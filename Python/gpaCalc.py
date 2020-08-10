while True:
    grade, total = 0, 0
    div = 25
    div2 = 1
    mode = input('Which mode do you want to use? (letter or number) > ')
    if mode.lower().startswith('l'):
        div = 1
        div2 = 0.04
    numClasses = int(input('How many classes? > '))
    for c in range(numClasses):
        grade = input('Enter your grade for Class %s. > ' %(c + 1))
        if 'a' in grade.lower():
            total += 4
        elif 'b' in grade.lower():
            total += 3
        elif 'c' in grade.lower():
            total += 2
        elif 'd' in grade.lower():
            total += 1
        elif 'f' in grade.lower():
            total += 0
        else:
            total += float(grade)
    print('Your GPA is %s.' %(round(total / (numClasses * div), 2)))
    totalGrade = total / numClasses / div2
    if 90 <= totalGrade <= 100:
        letter = 'n A'
        if totalGrade == 100:
            letter = 'n A+'
    elif 80 <= totalGrade <= 90:
        letter = ' B'
    elif 70 <= totalGrade <= 80:
        letter = ' C'
    elif 60 <= totalGrade <= 70:
        letter = ' D'
    else:
        letter = 'n F'
    print('You have an overall grade of %s, which is a%s.' %(round(totalGrade, 2), letter)) 
