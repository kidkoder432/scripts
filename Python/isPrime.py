import math
def isPrime(number):
    for div in range(2, int(math.sqrt(number))):
        equal = number % div
        if equal == 0:
            print('The number is composite.')
            print('It is divisible by ' + str(div))
            return
        else:
            pass
    print('The number is prime.')
    
def main():
    while True:
        print('Please enter a number')
        number = int(input())
        isPrime(number)

if __name__ == '__main__':
    main()
