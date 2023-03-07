import time
from typing import Union
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
import pyautogui
pyautogui.PAUSE = 0

from utils import stardew_focused, sanitize_key

class AnimationCancel:
    def __init__(self, watch_key: Union[Key, KeyCode, str]):
        self.key = sanitize_key(watch_key)
        self.down = False # use to ensure it only occurs once before release
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)

    def on_press(self, key: Union[Key, KeyCode, None]):
        if stardew_focused() and key == self.key and not self.down:
            self.down = True
            pyautogui.keyDown("shiftright")
            pyautogui.keyDown("r")
            pyautogui.keyDown("delete")
            pyautogui.sleep(0.025) # pause to allow it register the presses
            pyautogui.keyUp("shiftright")
            pyautogui.keyUp("r")
            pyautogui.keyUp("delete")

    def on_release(self, key: Union[Key, KeyCode, None]):
        if key == self.key:
            self.down = False
    
    def start(self):
        # start background thread
        self.listener.start()

    def stop(self):
        # stop background thread
        self.listener.stop()

    def run(self):
        # run as blocking thread
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

if __name__ == '__main__':
    import time
    # at some point I want to make a little ui or load a json file that allows us to swap what key we use
    ac = AnimationCancel(Key.space) # change this to whatever key you want, regular keyboard keys use "k"
    ac.run()
    while True:
        time.sleep(1)