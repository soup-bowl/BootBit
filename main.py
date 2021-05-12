import PySimpleGUI as sg
import subprocess
import json
import sys

icon = 'R0lGODlhfACAAPMKACIiIlVVVYiIiN0AAAC7AERERHd3dwAAAMzM/8zMzP///wAAAAAAAAAAAAAAAAAAACH5BAEAAAoALAAAAAB8AIAAAAT+UMlJqzo46827/2AojodlnqhErmzrimkcv3Rtg3Ju3nxP6zpNYkgsGo/IpHLJbDoTGiBK+Kxar1hmVLrLZL/g8HLLrVDF6DSWXJ6c1fB4kt2+eOX4PDRTp7z1gGJ0bX+Bhmt8fSp3SwWOj5CRkpOUlZaXjk2DZYVHmJ+goaCaiYqdRqKpqqmkGIqLGE2rs7SUrSWvp5AIvL2+v8DBwsPExbwGyAZzpX26j8bQ0dLRycpIm1zOjtPc3dzVy665jKjP3ufoweDXzHXaBenx8etH2FLv8vne9Eb2QPj6AlJLFg6XKXJFdglcSIxfEX9BEBJRyLDiL4dEIOYAaLEjAoz+QzTK4OixIsg94g7GQkKxJMOTImdIHNLSmAabGXBimAazHaGZCWoWuzk0Z9Gd0nqmbAZUKDGiT41GRToQWcFXdlZ6MhcN6jCvwsAWU2qQqdZy26SJBbb2V1thZLGS1HmArt2kBNktddeUK7S3vQDzEnwxbz2fnPqm7Sr1a+Owj8ca7oc4m2J4FQmfizvubEK/AjXvm/yw8r3LFkV346zyQBKn+VR/I53R9D/UmSPrY23WNUvQAWXzpB3SdkTPE4HrE47Xqt6yfJHTVB5bdz7e0X1vXVydg0XsP6UHpX7Ow3fiKKGH144W8/IO550f3rv+NXlv5k2ij5lirsuA4CX+Jh5s/82zn3Eb4VagQAFaNuB9C44mH2X0CcjeZ9xNIxtzwDR42oMZqmUdZFSh4+FtILrHzYYjNmfNfOpZaF+IjJV4VzonHndhcjSuuAKDB1bo4I7T9ajhjwAGGeOQM6pYHpK7KSmXguiwAOSEpQn5IZHjGRmhhC9SuOSWTX6ZJJa1aYkilwSaORuaxampY5luypNjginWaaeUnbEJoZ7G3DkSlYCuxmdrdBYK5lV9NlHNo5BGKumklFYq6S1TileEpZx26mmnmDbKxKeklkpqqIiOauqqrEaKam+HxJoFf1MAJeutz2XKJa68pjnmmr0Gm6uowhabnq7GGkvrCaf+JBvrsl1o6qwh0FrQ7LSBVGuGrdgCoq0f3Habx7duhCuuHOTCsuu5eKSb1brsxuHutfHCMa+59aJxr3gE9Otvv3r4wMGr2SXx778BC0zvscQacbC/CSssbZy/zonEwwCPK/HEDKd6xAAghwyyHq1SSnB9SIgsMsklX6oFgoOKp3LILLcM6ckypjzzADXbfFKWFeMJb776wiwTx0SHse/QSYOxdNMRBx0z01AjIqfQVbdrdH/4Zm3F017bu3WtSIf9BNhmF3311GmngXbbTo899cZ0C4wVs3Xn7cPd0ert9w98b/v34C0ELvgBASSu+OKMN674LABELvnklFdu+eWsHhgOLgaOd+455JeHLjrmHWheLueep7446KO3Pnrmpr+r+uwBsO767ZXDbroGPkPauSi4h6675rz3Xs3voQRPOgexv2v88Y4Dr3zupcde/PMGIA/K9NQzb30GAoQv/vjkl2/++JZq/0nrwxuuwfnwx09++tEn/3r1u4Mv//7n09+49KJrX+Dex78Coq9S6sME+/BHPMI5kATNe6AEQxDBCVrQe/m7oAalNoEIAAA7'

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
			[sg.Button(key=entry['name'], image_filename=entry['logo'], size=(5,5))],
			[sg.Text(entry['name'])]
		], element_justification='c')
	)

layout = [
	[sg.Image(data=icon)],
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
