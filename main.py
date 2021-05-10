import PySimpleGUI as sg

welcomeLabel = "Choose an Operating System to begin."

layout = [
	[sg.Text(welcomeLabel, justification='center', size=(200,1))],
	[
		sg.Button('', key='sys9', image_filename='./logo-apple.png'),
		sg.Button('', key='dos', image_filename='./logo-windows.png')
	],
	[sg.Cancel('Exit', key='quit', auto_size_button=True)]
]

window = sg.Window(welcomeLabel, layout, element_justification='c', resizable=True, auto_size_buttons=True).finalize()
window.maximize()

while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'quit'):
        break

window.close()
