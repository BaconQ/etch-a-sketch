from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def move_fd():
    tom.forward(20)

def move_bw():
    tom.forward(-20)

def turn_right():
    tom.right(10)

def turn_left():
    tom.left(10)

def clear():
    tom.setposition(0,0)
    tom.setheading(0)
    tom.clear()


screen.onkey(key="w", fun= move_fd)
screen.onkey(key="s", fun= move_bw)
screen.onkey(key="d", fun= turn_right)
screen.onkey(key="a", fun= turn_left)
screen.onkey(key="c", fun= clear)

screen.listen()
screen.exitonclick()


