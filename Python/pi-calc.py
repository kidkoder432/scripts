it = []
itn = []
def piCalc(repeat):
    x = 1
    pi = 0
    for i in range(repeat):
        it.append(pi)
        pi = pi + (4/x) - (4/(x + 2))
        print(pi)
        x += 4
piCalc(10000)
print('\n' * 15)
def nilakantha(repeat):
    pi = 3
    x, y, z = [2,3,4]
    for i in range(repeat):
        itn.append(pi)
        pi += 4/(x*y*z) - 4/((x + 2) * (y + 2) * (z + 2))
        x+= 4; y+=4; z+=4
        print(pi)
    return pi
print(nilakantha(10000000))

#import matplotlib.pyplot as plt
#plt.plot(it, list(range(10)))

#plt.plot(itn, list(range(10)))
#plt.xlabel('Value of pi')
#plt.ylabel('Number of Iterations')
#plt.show()
