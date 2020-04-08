import pyautogui, time
import typePrint as t
#for i in range(100):
 #   t.append(str(i))
#t = ', '.join(t)
while True:   
    whatToType = input('Please enter a string of text to type: ')
    if input('Should I start typing?(y/n): ').lower().startswith('y'):
        time.sleep(5)
        print('Starting...')
        for l in list(whatToType):
            pyautogui.press(l)
            #time.sleep(0.05)
    t.typePrint(whatToType, 0.04)
    io = 687497669079867908765890675680975687984751345984956879465874657435643057643756403564275647540354365794864978564904757493749863758164785658496754967698676871675471451645363643453824378494637463849343648340366765715464567145656745481562457578456384565787856751988696734679856748197856974856147856406084543957864