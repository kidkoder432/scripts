import time
import os
import datetime # will be used in future
days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
        4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
for i in days.keys():
    fileName = days[i] + '.txt'
    print(fileName)
    f = open(fileName, 'a+')
    f.close()
print('Please enter a day to add to your log of practice')
day = input()
name = day + '.txt'
try:
    f = open(name, 'a')
    print('Enter the type of practice, then the number of minutes.')
    practice = input()
    minutes = input()
    # Make a function to use the days of the week and calculate if the file is empty.
except:
    print('Invalid input. Try again.')

