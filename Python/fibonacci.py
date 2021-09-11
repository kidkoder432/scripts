num = 1
def fib(num):
    fiblist = [0, 1]
    a = 0
    b = 1
    if num <= 0:
        print('Error. Invalid input.')
        return 1
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    elif num == 3:
        return 1
    else:
        for i in range(num - 2):
            ans = a + b
            a = b
            b = ans
            #print(ans)
            fiblist.append(ans)
        import pprint
        #pprint.pprint(fiblist)
        return ans
f = open('fib.txt', 'w')
for i in range(12000):
    try:
        num += 1
        total = fib(num)
        print(f.write(str(total) + '\n'), end='\r')
        print(fib(num + 1) / fib(num))
    except Exception as exc:
        print('\n\n', exc)
    
f.close()
