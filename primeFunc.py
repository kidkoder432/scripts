import math
nums = []
def sieve(n):
    sqrt = math.sqrt(n)
    for i in range(1, int(sqrt) + 1):
        nums.append(str(i))
    nums.remove('1')
    for i in range(2, int(sqrt)):
        for k in nums:
           mod = int(k) % i
           if mod == 0:
                nums.remove(k)
    print(' '.join(nums))
    return

while True:
    n = int(input('enter a number '))
    sieve(n)
