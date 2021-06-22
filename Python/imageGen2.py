import random
b = []
for x in range(250000):
    for i in range(8):
        b.append(str(random.choice([0, 1])))
    b.append(' ')
del b[-1]
del b[0]
b = ''.join(b)
print(b[:100])
f = open('bin.txt', 'w')
for x in b.split(' '):
    print(chr(int(x, 2)), end='')
    f.write(x)
f.close()