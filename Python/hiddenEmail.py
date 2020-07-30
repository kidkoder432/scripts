import pyperclip, random
def genRandomText(length):
    text = []
    sym = list('''`1234567890-=\][poiuytrewqasdfghjkl;'/.,mnbvcxz?><MNBVCXZASDFGHJKL:"}{POIUYTREWQ~!@#$%^&*()_+''').append(' ')
    for i in range(length):
        text.append(random.choice(sym))
    return ''.join(text)    
msg = input('Enter a message > ')
copy = genRandomText(587349) + '| ' + msg + ' |' + genRandomText(956832)
pyperclip.copy(copy)
print('The message has been copied to the clipboard.')