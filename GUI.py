import PySimpleGUI as sg

theme = sg.theme('DarkBlue13')
window = sg.FlexForm('QUIKSend')

layout = [
    [sg.Text('Fill in the information below and click SEND when you are ready!')],
    [sg.Text('Your Email', size=(11, 1)), sg.InputText()],
    [sg.Text('Your Password', size=(11, 1)), sg.InputText()],
	[sg.Text('', size=(11, 1))],

	[sg.Text('Receiver Email:', size=(11, 1)), sg.InputText()],
	[sg.Text('Subject:', size=(11, 1)), sg.InputText()],
	[sg.Text('Message', size=(11, 1)), sg.InputText()],
	[sg.Text('', size=(11, 1))],
	[sg.Output(size=(59, 1))],
	[sg.Button('SEND'), sg.Button('EXIT')],
	]

button, values = window.Layout(layout).Read()