import os
import sys
monthDay = {'January': 31,'Feburary': 28,'March': 31,'April': 30,
    'May': 31,'June': 30,'July': 31,'August': 31,
    'September': 30,'October': 31,'November': 30,'December': 31}
keys = list(monthDay.keys())
def makeDayFiles():
    if year % 4 == 0:
        f = open('Feburary 29.txt', 'a+')
        f.close()
    else:
        pass
    
    index = 0
    for i in monthDay.values():
        for k in range(i):
            fileName = keys[index] + ' ' + str(k + 1) + '.txt'
            f = open(fileName, 'a+')
            f.close()
           # print(fileName)
        index += 1
def writeTimes(fileName):
    global contents
    if os.stat(fileName).st_size == 0:
        f = open(fileName, 'w')
        f.write('''
    6:00          
    6:30
    7:00          
    7:30          
    8:00
    8:30
    9:00
    9:30
    10:00
    10:30
    11:00
    11:30
    12:00
    12:30
    13:00
    13:30
    14:00
    14:30
    15:00
    15:30
    16:00
    16:30
    17:00
    17:30
    18:00
    18:30
    19:00
    19:30
    20:00
    20:30
    21:00
    21:30
    22:00
    23:30
    23:00
    23:30
    0:00''')
    else:
        pass
    f = open(fileName, 'r')
    contents = f.read()
    f.close()
print('Which year is it?')
year = int(input())
makeDayFiles()
while True:
    print('Would you like to view your calendar, or edit it?')
    ans = input()
    if ans.lower() == 'view':
        while True:
            try:
                print('Please enter the date. (month, day)')
                month = input()
                month = month.title()
                day = input()
                fileName = month + ' ' + str(day) + '.txt'
                if os.stat(fileName).st_size == 0:
                    print('This file is empty.')
                else:
                    d = open(fileName, 'r')
                    print('File content: \n' + d.read())
                break
            except:
                print('Invalid input. Try again.')
    elif ans.lower() == 'edit':
        print('Would you like to add any events?')
        ans = input()
        if ans.lower() == 'yes':
            while True:
                try:
                    print("Enter the date, months then days.")
                    month = input()
                    month = month.title()
                    day = input()
                    print('Opening %s %s.txt' % (month, day))
                    fileName = str(month) + ' ' + str(day) + '.txt'
                    writeTimes(fileName)
                    print('Type the hour, followed by the minutes, then your event.')
                    hours = input()
                    minutes = input()
                    event = input()
                    f = open(fileName, 'w')
                    time = hours + ':' + minutes
                    contents = contents.replace(time, time + '          ' + event)
                    addedItems = time + '          ' + event
                    f.write(contents)
                    f.close()
                    file = open(fileName, 'r')
                    print('File content: ')
                    print('\n' + file.read())
                    file.close()
                    break
                except:
                    print('Invalid input. Try again.')
        else:
            pass
    print('Press Enter to quit, or press Space + Enter to continue.')
    x = input()
    if len(x) == 0:
         sys.exit()
    else:
        pass

