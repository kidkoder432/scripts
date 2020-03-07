import pprint, time
while True:
    msg = input('Enter a message to count its words. > ')
    count = {}
    msg2 = msg.split()
    for l in msg2:
        if l == '.' or ',' or ':' or '"':
           msg3 = msg.replace(l, '')
    for word in msg.split(' '):            
        count.setdefault(word, 0)
        count[word] += 1
    pprint.pprint(count)
    print('Words: ' + str(len(msg.split(' '))))
    
