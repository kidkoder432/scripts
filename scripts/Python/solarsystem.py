import turtle as t
t.speex(0)
t.right(90)
t.colormode(255)
t.ht()
t.bgcolor(0, 0, 0)
t.pencolor(255, 255, 255)
t.pu()
t.fd(100)
t.left(90)
t.pd()
t.circle(200)
t.pencolor(255, 230, 0)
t.fillcolor(255, 230, 0)
t.pu()
t.goto(0, 50)
t.pd()
t.begin_fill()
t.circle(50)
t.end_fill()
t.pu()
t.goto(0, 0)
earth = t.Turtle()
t.pencolor(0, 200, 255)
t.pu()
shape = t.Shape('compound')
t.pu()
t.begin_poly()
t.circle(25)
t.end_poly()
shape.addcomponent(t.get_poly(), (0, 200, 255))
t.register_shape('earth', shape)
earth.shape('earth')
earth.pu()
moon = t.Turtle()
shape = t.Shape('compound')
t.begin_poly()
t.circle(10)
t.end_poly()
shape.addcomponent(t.get_poly(), (255, 255, 255))
t.register_shape('moon', shape)
moon.shape('moon')
earth.goto(0, -100)
moon.speed(10)
moon.pencolor(255, 255, 255)
while True:
    earth.fd(3.5)
    earth.lt(1)
    moon.goto(earth.xcor() + 80, earth.ycor())
    

        






