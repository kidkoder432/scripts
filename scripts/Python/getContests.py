
import requests, bs4

def getContests(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('')
    text = elems[0].text.strip()
    f = open(contest, 'w')
    f.write(text)
    f.close()
print('Please enter the type of contest.')
contestType = input()
##print('Please enter the year of the contest.')
##year = input()
contestType = contestType
contestType.replace(' ', '_')
contest = contestType
webAddress = 'https://artofproblemsolving.com/wiki/index.php/' + contest
getContests(webAddress)






        
