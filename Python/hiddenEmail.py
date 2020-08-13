import pyperclip, random, smtplib, pyinputplus as pyip
def genRandomText(length):
    text = []
    sym = list('''`1234567890-=\][poiuytrewqasdfghjkl;'/.,mnbvcxz?><MNBVCXZASDFGHJKL:"}{POIUYTREWQ~!@ #$%^&*()_+''')
    for i in range(length):
        text.append(random.choice(sym))
    return ''.join(text)    
msg = input('Enter a message > ')
cop = genRandomText(873459) + '| ' + msg + ' |' + genRandomText(565682)
user = input('Enter email address: ')
pw = pyip.inputPassword('Enter password: ')
to = input('Enter recipent email address: ')
con = smtplib.SMTP('smtp.gmail.com', 587)
con.ehlo()
con.starttls()
con.login(user, pw)
con.sendmail(user, to, 'Subject: A hidden email\n\n' + cop)
con.quit()
