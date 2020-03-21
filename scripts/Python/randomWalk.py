import binList
charList = []
for n in binList.binList:
    if n != '1':
        print('_')
        charList.append('_')
        continue
    print(' ' + '|')
        
