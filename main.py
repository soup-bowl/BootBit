import PySimpleGUI as sg

welcomeLabel = "Choose an Operating System to begin."

colApple = sg.Column([ [sg.Button(key='sys9', image_filename='./logo-apple.png')], [sg.Text('System 7')] ], element_justification='c')
colWin   = sg.Column([ [sg.Button(key='dos', image_filename='./logo-windows.png')], [sg.Text('DOS')] ], element_justification='c')

layout = [
	[sg.Image('./logo-happymac.gif')],
	[sg.Text(welcomeLabel, size=(200,1))],
	[colApple, colWin],
	[sg.Cancel('Exit', key='quit', auto_size_button=True)]
]

window = sg.Window(
	welcomeLabel,
	layout=layout,
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
