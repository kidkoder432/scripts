def progressReport():
    f = open('googolplex.txt')
    percent = ((i + 1)/ (10 ** 100) * 100) + 1
    print('Percent completed: %s' %(int(percent)))
    print('Iterations completed: %s' %(i))
    f.close()

import time, pyautogui as p
start = time.time()
f = open('googolplex.txt', 'w')
f.write('1')

for i in range(pow(10, 100)):
    f.write('0')
    if i % 1000000 == 0:
        progressReport()
        p.press(' ')
        

f.close()


end = time.time()
import smtplib as s

sender = 'findprajju@gmail.com'
receivers = ['findprajju@gmail.com']

message = 'Program finished.\nTime taken: ' + str(end - start) 


try:
   smtpObj = s.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except s.SMTPException:
   print("Error: unable to send email")
