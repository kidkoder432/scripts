import random, time
factors = []
def getFactors(num):
    for div in range(1, (int(num / 2) + 1)):
        a = num % div
        if a == 0:
            factors.append(div)

def s(n):
    total = 0
    getFactors(n)
    for f in factors:
        total = total + f
    return total

total = random.randint(0, 10000)
print(total)
while s(total) != 0:
    total = s(total)
    print('The function s(n) returned ' + str(total))
    for i in range(len(factors)):
        factors.remove(factors[0])
    
    
    
