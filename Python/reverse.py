import pyautogui as p
import pyperclip
msg = pyperclip.paste().split()
for i in range(len(msg) - 1, -1, -1):
    p.press(msg[i]

