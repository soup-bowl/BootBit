import PySimpleGUI as sg

sg.theme('SystemDefault1')

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
	auto_size_buttons=True	
).finalize()

window.maximize()

while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'quit'):
        break

window.close()
