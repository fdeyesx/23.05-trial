from turtle import *
tracer(0)
screensize(5000,5000)
left(90)
k = 15

for i in range(2):
    forward(10*k)
    right(90)
    forward(20*k)
    right(90)
up()
forward(3*k)
right(90)
forward(7*k)
left(90)
down()
for i in range(2):
    forward(70*k)
    right(90)
    forward(90*k)
    right(90)

up()
for x in range(0,100):
    for y in range(0,100):
        goto(x*k,y*k)
        dot(3)
goto(0,0)
dot(5,'red')
done()
