#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import PyDictionary as pyd

words = pyd.PyDictionary()
while True:
    word = input('Enter a word: ')
    print(words.meaning(word))


