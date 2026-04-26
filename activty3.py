import turtle
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.title("Turtle")
j = turtle.Turtle()

size = 0
while True:
    for i in range(4):
        j.fd(size+1)
        j.left(90)
        size = size - 5
    size = size + 1    