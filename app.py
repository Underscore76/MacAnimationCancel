import threading
import PySimpleGUI as sg
import pyautogui
from pynput.keyboard import Key
pyautogui.PAUSE = 0

from ac_3_to_1 import AnimationCancel

ac = AnimationCancel(Key.space)
threading.Thread(target=ac.run, daemon=True).start()

layout = [
    [sg.Text("3 to 1 AC bound to Space")],
    [sg.Text("Will run in background")],
]

window = sg.Window(
    title="SDVAC", 
    layout=layout,
    icon="Resources/icon.ico"
)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values)
    pass

# ac.stop()
window.close()