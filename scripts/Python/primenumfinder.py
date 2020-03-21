import isPrime
while True:
    print('Please enter the number of digits your prime should have.')
    length = int(input())
    num = '1' + '0' * (length - 1)
    while len(str(num)) != length + 1:
        if isPrime.isPrime(num) == True and length == len(str(num)):
            f = open('prime.txt', 'w')
            f.write(str(num))
            f.close()
            print(num)
            break
        else:
            num = int(num)
            num+=1
        
