import webbrowser, sys, pyperclip
sys.argv
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]

webbrowser.open('https://google.com/maps/place/' + address)
    

