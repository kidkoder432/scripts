avg = 0
def average(numbers):
    numbers = numbers.split()
    listlen = len(numbers)
    total = 0
    for i in numbers:
        total += int(i)
    avg = total / listlen

while True:
    print('Please enter a group of numbers seperated by spaces.')
    numbers = input()
    average(numbers)
    print('The average is %s' %(avg))
