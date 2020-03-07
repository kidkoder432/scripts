
def fib(num):
    fiblist = [0, 1]
    a = 0
    b = 1
    if num <= 0:
        print('Error. Invalid input.')
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
while True:
    num = int(input('Please enter the point of the Fibonacci sequence that you want to see.'))
    total = fib(num)
    print('The number is %s' %(total))
