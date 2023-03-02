from typing import Any, Union
from pynput.keyboard import Key, KeyCode

try:
    from Cocoa import NSWorkspace
    def get_active_app() -> dict:
        """pull the frontmost application out of the workspace"""
        return NSWorkspace.sharedWorkspace().activeApplication()

    def stardew_focused() -> bool:
        """check if stardew bundle id matches"""
        app = get_active_app()
        return app.get("NSApplicationBundleIdentifier",None) == "com.concernedape.stardewvalley"
except:
    def stardew_focused() -> bool:
        """default to always use if unable to load platform specific resource"""
        return True



def sanitize_key(key: Any) -> Union[Key, KeyCode]:
    """takes in a key and attempts to sanitize it into a Key or KeyCode type"""
    if isinstance(key, (Key, KeyCode)):
         return key
    
    if isinstance(key, str):
         return KeyCode.from_char(key)
    
    raise Exception(f"unknown key type: {key} is {type(key)}. Must be string or `Key` type")