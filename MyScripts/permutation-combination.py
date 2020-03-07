import math
def permutation(items, choose, repetition):
    if repetition == 'True':
        print('The number of permutations is ' + str(items**choose) + '.')
    elif repetition == 'Partial':
        number = (math.factorial(items)) / (math.factorial(items - choose))
        print('The number of permutations is ' + str(number) + '.') 
    else:    
        print('The number of permutations is ' + str(math.factorial(items)) + '.')


def combination(items, choose, repetition):
    if repetition == 'True':
        number3 = (math.factorial(choose + items - 1)) / (math.factorial(choose)) * (math.factorial(items - 1))
        print('The number of combinations is ' + str(number3) + '.')
    else:
        number2 = (math.factorial(items)) / (math.factorial(choose)) * (math.factorial(items - choose))
        print('The number of combinations is ' + str(number2) + '.')

        

x = int(input())
y = int(input())
z = input()
permutation(x, y, z)
a = int(input())
b = int(input())
c = input()
combination(a, b, c)
