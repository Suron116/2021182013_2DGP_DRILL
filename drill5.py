import turtle

turtle.shape('turtle')

def w_up():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def a_left():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)

def s_down():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)

def d_right():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

def esc_reset():
    turtle.reset()

turtle.onkey(w_up, 'w')
turtle.onkey(a_left, 'a')
turtle.onkey(s_down, 's')
turtle.onkey(d_right, 'd')
turtle.onkey(esc_reset, 'Escape')
turtle.listen()
