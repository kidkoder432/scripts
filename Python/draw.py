import turtle
while True:
    sides = int(input("How many sides? > "))
    for i in range(sides):
        turtle.forward(5)
        turtle.right(sides / 360)
