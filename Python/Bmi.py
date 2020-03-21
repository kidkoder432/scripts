

def bmi(height, weight):    
    bmi = 0
    weight = weight * 703
    height = height * height
    bmi = weight / height
    print('Your BMI is ' + str(bmi) +'.')
    if bmi >= 18 and bmi <= 25:
            print('You are in good health.')
    elif bmi < 18:
        print('You are underweight.')
    elif bmi > 25:
        print('You are overweight.')
    return(bmi)
while True:
    print('Please enter your height in inches and your weight in pounds.')
    height = int(input())
    weight = int(input())
    bmi(height, weight)
