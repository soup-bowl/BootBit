import PySimpleGUI as sg
import subprocess
import json
import sys

sg.theme('SystemDefault1')
data = None
try:
	with open("./config.json") as json_file:
		data = json.load(json_file)
except FileNotFoundError:
	msg = 'No configuration file found. A config.json file is required.'
	sg.Popup(msg, title='config.json missing', keep_on_top=True)
	print(msg)
	sys.exit(1)

font = 'Arial 16'

exeApple = './Mini_vMac_ARM'
exeDOS   = 'dosbox'

welcomeLabel = "Choose an Operating System to begin."

columns = []
for i, entry in enumerate(data['options']):
	columns.append(
		sg.Column([
			[sg.Button(key=entry['name'], image_filename=entry['logo'], pad=(5,5))],
			[sg.Text(entry['name'])]
		], element_justification='c')
	)

layout = [
	[sg.Image('./assets/logo-happymac.gif')],
	[sg.Text(welcomeLabel)],
	columns,
	[sg.Cancel('Exit', key='quit'), sg.Button(button_text='Shutdown', key='shut')]
]

window = sg.Window(
	welcomeLabel,
	layout=layout,
	element_justification='c',
	text_justification='c',
	resizable=True,
	auto_size_buttons=True,
	font=font
).finalize()

window.maximize()

while True:
	event, values = window.read()

	if event == 'shut':
		process = subprocess.Popen(['sudo', 'shutdown', '-r', 'now'])
		break;

	if event in (sg.WIN_CLOSED, 'quit'):
		break
	
	for entry in data['options']:
		if event == entry['name']:
			try:
				op_path = None if not entry['cwd'] else entry['cwd']

				print("Executing '"+ entry['command'] + ("." if op_path == None else "' (in directory '" + op_path + "').") )
				process = subprocess.Popen(entry['command'].split(), cwd=op_path)
			except IndexError:
				sg.Popup('No command specified.', title='No runner specified', keep_on_top=True)
				print("Failed, no command found.")
			except FileNotFoundError:
				sg.Popup('Couldn\'t find the requested application.', title='No application', keep_on_top=True)
				print("Failed, no application found.")

window.close()
