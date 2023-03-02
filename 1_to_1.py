from typing import Union
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
import pyautogui

from utils import stardew_focused, sanitize_key

class AnimationCancel:
    def __init__(self, 
            delete_key: Union[Key, KeyCode, str], 
            rshift_key:Union[Key, KeyCode, str], 
            r_key:Union[Key, KeyCode, str]
        ):
        self.keys = {
            "delete": {"down": False, "key": sanitize_key(delete_key)},
            "shiftright": {"down": False, "key": sanitize_key(rshift_key)},
            "r": {"down": False, "key": sanitize_key(r_key)}
        }
    
    def on_press(self, key: Union[Key, KeyCode, None]):
        if stardew_focused():
            # for each key in the watch list that's not already down, check if it should get set down
            for watch_key in self.keys:
                if key == self.keys[watch_key]["key"] and not self.keys[watch_key]["down"]:
                    pyautogui.keyDown(watch_key)
                    self.keys[watch_key]["down"] = True
            
    def on_release(self, key):
        # for each key in the watch list that's not up, check if it should get set up
        for watch_key in self.keys:
            if key == self.keys[watch_key]["key"] and self.keys[watch_key]["down"]:
                pyautogui.keyUp(watch_key)
                self.keys[watch_key]["down"] = False
    
    def run(self):
        pyautogui.PAUSE = 0
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

# at some point I want to make a little ui or load a json file that allows us to swap what key we use
ac = AnimationCancel(
    delete_key=Key.space,
    rshift_key="v", # change this to whatever key you want
    r_key="b" # change this to whatever key you want
)
ac.run()