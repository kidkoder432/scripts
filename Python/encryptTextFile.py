import random
def encrVigenere(key, msg):
        # Vigenere Cipher (Polyalphabetic Substitution Cipher)
    # https://www.nostarch.com/crackingcodes/ (BSD Licensed)


    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


    def encryptMessage(key, message):
        return translateMessage(key, message, 'encrypt')


    def decryptMessage(key, message):
        return translateMessage(key, message, 'decrypt')


    def translateMessage(key, message, mode):
        translated = [] # Stores the encrypted/decrypted message string.
        keyIndex = 0
        key = key.upper()

        for symbol in message: # Loop through each symbol in message.
            num = LETTERS.find(symbol.upper())
            if num != -1: # -1 means symbol.upper() was not found in LETTERS.
                if mode == 'encrypt':
                    num += LETTERS.find(key[keyIndex]) # Add if encrypting.
                elif mode == 'decrypt':
                    num -= LETTERS.find(key[keyIndex]) # Subtract if decrypting.

                num %= len(LETTERS) # Handle any wraparound.

                # Add the encrypted/decrypted symbol to the end of translated:
                if symbol.isupper():
                    translated.append(LETTERS[num])
                elif symbol.islower():
                    translated.append(LETTERS[num].lower())

                keyIndex += 1 # Move to the next letter in the key.
                if keyIndex == len(key):
                    keyIndex = 0
            else:
                # Append the symbol without encrypting/decrypting:
                translated.append(symbol)
        return ''.join(translated)
        
    return translateMessage(key, msg, 'encrypt') 

def genRandomText(length):
	seq = []
	sym = list(r'1234567890-=\][poiuytrewqasdfghjkl;/.,mnbvcxz!@#$~`%^&*()_+|}{POIUYTREWQASDFGHJKL:"?><MNBVCXZ"}')
	for i in range(length):
		seq.append(random.choice(sym))
	return ''.join(seq)
msg = input('Enter message to send > ')
key = input('Enter key > ')

emailtext = encrVigenere(key, msg) + '''

Go to http://decrypt.prajwalagrawal.repl.run to decrypt''' +'''

''' + genRandomText(random.randint(0, 10001)) + '| ' + key + ' |' + genRandomText(random.randint(0, 10001))
fpath = input('Please enter the file path where the text file will be saved. For example: "C:\\Users\\[username]\\Documents > ')
f = open(fpath + '\\ciphertext.txt', 'w+')
f.write(emailtext)
f.close()
print(r'The ciphertext and key have been copied to a text file called ciphertext.txt located in '+ fpath + r'\ciphertext.txt' + '. You can copy/paste the text into an email, or just keep it on your computer.')
