#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, bs4, time, smtplib
while True:
    res = requests.get('https://mathcircle.berkeley.edu/math-taught-right-way-program')
    res.raise_for_status()
    html = res.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    d = soup.select('body > div > div:nth-child(3) > div > section > div.region.region-content > article > div > div > table > tbody > tr:nth-child(2) > td.text-align-center')[0].getText()
    if d != 'Applications will become available late October, or earlier.':
        print('Class available!')
        con = smtplib.SMTP('smtp.gmail.com', 587)
        con.ehlo()
        con.login('findprajju@gmail.com', 'prajwal08')
        con.starttls()
        con.sendmail('findprajju@gmail.com', 'agrawal.pj@gmail.com', 'Subject: motr class available\n\nThe class Math Taught The Right Way is available.')
        con.quit()
    else:
        print('Not Available')
    time.sleep(600)
##    word = input('Enter a word: ')
##    url = 'https://m-w.com/dictionary/%s' %(word)
##    res = requests.get(url)
##    try:
##        res.raise_for_status()
##    except Exception as e:
##        print('That word isn\'t in the dictionary. Please try again')
##        continue
##    html = res.text
##    soup = bs4.BeautifulSoup(html, 'html.parser')
##    defin = soup.select('#dictionary-entry-1 > div.vg > div.sb > span.sb-0 > div > span.dt > span')
##    try:
##        print('Definition: %s' %(defin[0].getText()))
##    except IndexError:
##        print('No definition found. Output was %s' %(defin))
