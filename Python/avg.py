def average(numbers):
    listlen = len(numbers)
    global avg
    avg = 0
    total = 0
    for i in numbers:
        total += float(i)
    avg = total / listlen
    return avg

while True:
    l = [-7897, 2, 78]
    l.append(0)
    print(average(l), end='\r')
