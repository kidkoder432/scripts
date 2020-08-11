import pyperclip, random
def genRandomText(length):
    text = []
    sym = list('''`1234567890-=\][poiuytrewqasdfghjkl;'/.,mnbvcxz?><MNBVCXZASDFGHJKL:"}{POIUYTREWQ~!@ #$%^&*()_+''')
    for i in range(length):
        text.append(random.choice(sym))
    return ''.join(text)    
msg = input('Enter a message > ')
cop = genRandomText(87349) + '| ' + msg + ' |' + genRandomText(56682)
pyperclip.copy(cop)
print('The message has been copied to the clipboard.')