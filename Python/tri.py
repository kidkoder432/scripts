def tri(seq):
    output = seq
    while seq > 0:
        output += seq - 1
        seq -= 1
    return output
while True:
    print('enter a number.')
    n = int(input())
    print(tri(n))
