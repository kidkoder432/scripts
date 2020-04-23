    #friendliness test - how friendly are two people?
while True:    
    ci = 0
    person1 = input('What is your name? > ')
    person2 = input('What is your friend\'s name? > ')
    print('Now we look at your interests. Enter these as words followed by spaces. For example, "reading math science"')
    p1interests = input('What are your interests? > ').split()
    p2interests = input('What are your friend\'s interests? >').split()
    print('Calculating...')
    for i in range(10000000):
        print(end = '')
    if len(p1interests) > len(p2interests):
        for i in p1interests:
            if i in p2interests:
                ci += 1
    else:
        for i in p2interests:
            if i in p1interests:
                ci += 1

    if ci >= 3:
        print('You two are both friends. I wish you a good life and well wishes.')
    elif ci == 2:
        print('A slightly shaky friendship lies ahead. Proceed with caution')
    elif ci == 1:
        print('Hmm... maybe I was wrong about this.')
    else:
        print('WARNING: STEP AWAY FROM EACH OTHER NOW.')
    


