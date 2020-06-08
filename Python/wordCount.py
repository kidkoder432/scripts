import pprint
while True:
    msg = input('Enter a message to count its words. > ')
    print('Words: %s' %(len(msg.split(' '))))
