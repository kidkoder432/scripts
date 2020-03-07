def piCalc(repeat):
    x = 1
    pi = 0
    for i in range(repeat):
        pi = pi + (4/x) - (4/(x + 2))
        x += 4
    print(pi)
piCalc(10 ** 40)
