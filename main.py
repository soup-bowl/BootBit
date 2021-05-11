import PySimpleGUI as sg
import subprocess

sg.theme('SystemDefault1')
font = 'Arial 16'

exeApple = './Mini_vMac_ARM'
exeDOS   = 'dosbox'

welcomeLabel = "Choose an Operating System to begin."

colApple = sg.Column([ [sg.Button(key='sys9', image_filename='./logo-apple.png', pad=(5,5))], [sg.Text('System 7')] ], element_justification='c')
colWin   = sg.Column([ [sg.Button(key='dos', image_filename='./logo-windows.png', pad=(5,5))], [sg.Text('DOS')] ], element_justification='c')

layout = [
	[sg.Image('./logo-happymac.gif')],
	[sg.Text(welcomeLabel)],
	[colApple, colWin],
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
	try:
		if event == 'sys9':
			process = subprocess.Popen(exeApple.split(), cwd='/home/pi/Macintosh')

		if event == 'dos':
			process = subprocess.Popen(exeDOS.split())
	except IndexError:
		sg.Popup('No command specified.', title='No runner specified', keep_on_top=True)
	except FileNotFoundError:
		sg.Popup('Couldn\'t find the requested application.', title='No application', keep_on_top=True)

	if event == 'shut':
		process = subprocess.Popen(['sudo', 'shutdown', '-r', 'now'])
		break;

	if event in (sg.WIN_CLOSED, 'quit'):
		break

window.close()
