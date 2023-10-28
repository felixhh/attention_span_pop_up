import PySimpleGUI as sg
import time

reminder_running = False
reminder_minutes = 0

def show_reminder(minutes):
    global reminder_running, reminder_minutes

    seconds = minutes
    time.sleep(seconds)  # Wait for the first interval

    while reminder_running:
        sg.popup(f'Time to focus for {minutes} minutes!', title='Reminder')
        time.sleep(seconds)

layout = [
    [sg.Text('Enter reminder time (minutes):')],
    [sg.InputText(key='minutes')],
    [sg.Button('Set Reminder'), sg.Button('Exit')],
]

window = sg.Window('Focus Reminder', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Set Reminder':
        minutes = int(values['minutes'])
        if minutes > 0:
            if not reminder_running:
                reminder_running = True
                reminder_minutes = minutes
                show_reminder(reminder_minutes)
            else:
                sg.popup('A reminder is already running. Close the reminder window to reset the timer.')
        else:
            sg.popup('Please enter a valid reminder time in minutes.')

window.close()
