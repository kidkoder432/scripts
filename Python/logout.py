import keyboard, mouse, time
while True:
    now = time.time()
    if not keyboard.is_pressed() and time.time() - now == 300:
        keyboard.press_and_release('ctrl+alt+delete', 'down', 'enter')
        
    