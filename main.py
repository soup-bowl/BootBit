import PySimpleGUI as sg

welcomeLabel = "Choose an Operating System to begin."
bgColor      = 'black'

colApple = sg.Column([ [sg.Button('', key='sys9', image_filename='./logo-apple.png')], [sg.Text('System 7')] ], element_justification='center')
colWin   = sg.Column([ [sg.Button('', key='dos', image_filename='./logo-windows.png')], [sg.Text('DOS')] ], element_justification='center')

layout = [
	[sg.Image('./Happy_Mac.gif')],
	[sg.Text(welcomeLabel, size=(200,1))],
	[colApple, colWin],
	[sg.Cancel('Exit', key='quit', auto_size_button=True)]
]

window = sg.Window(
	welcomeLabel,
	layout,
	element_justification='c',
	text_justification='c',
	resizable=True,
	auto_size_buttons=True	
).finalize()

window.maximize()

while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'quit'):
        break

window.close()
