from pynput import keyboard
from pynput.keyboard import Key
import pyautogui

from utils import stardew_focused

class AnimationCancel:
    def __init__(self, watch_key: Key):
        self.key = watch_key

    def on_press(self, key):
        if stardew_focused():
            if key == self.key:
                pyautogui.keyDown("delete")
                pyautogui.keyDown("shiftright")
                pyautogui.keyDown("r")
    
    def on_release(self, key):
        if key == self.key:
            pyautogui.keyUp("delete")
            pyautogui.keyUp("shiftright")
            pyautogui.keyUp("r")
    
    def run(self):
        pyautogui.PAUSE = 0
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

# at some point I want to make a little ui or load a json file that allows us to swap what key we use
ac = AnimationCancel(
    watch_key=Key.space, # change this to whatever key you want, regular keyboard keys use "k"
)
ac.run()