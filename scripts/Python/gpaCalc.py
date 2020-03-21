while True:
    classes = []
    grade = 0
    total = 0
    numClasses = int(input('How many classes? >'))
    for c in range(numClasses):
        grade = input('Enter your grade for Class %s.' %(c + 1))
        total += float(grade)
    print('Your GPA is %s.' %(round(total / (numClasses * 100 / 4), 2)))
    totalGrade = total / numClasses
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
