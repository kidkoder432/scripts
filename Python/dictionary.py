# #! python3
# # downloadXkcd.py - Downloads every single XKCD comic.
import bs4, requests

# import PyDictionary as pyd

# words = pyd.PyDictionary()
# while True:
#     word = input('Enter a word: ')
#     print(words.meaning(word))
while True:
    word = input("Enter a word: ")
    url = f"https://www.merriam-webster.com/dictionary/{word}"
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    elem = soup.select(
        "#dictionary-entry-1 > div.vg > div > span"
    )
    print(elem[0].text)
