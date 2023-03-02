# MacOS Animation Canceling

Huge shoutout to growthmindset#4583 on discord for the basis of these tools! They did all the hard work figuring out pynput/pyautogui tie ins :)

## Getting Started

Right now this repo expects that you have python installed on your machine.

1) Install dependencies
- `pip install -r requirements.txt`
- inputs are listened for using `pynput` and then new keys are sent using `pyautogui` (for some reason neither of us could figure out how to get `pynput` to send stuff)

2) Modify the key you'd like to use in your desired script.
- In `pynput` things like `ctrl` and `space` are called via `Key.space` (etc) but normal keyboard keys like `a` and `b` you can choose by just passing the string `"a"` or `"b"`.

3) Run the script, tab to Stardew and get canceling