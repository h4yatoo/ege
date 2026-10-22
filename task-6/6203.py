from turtle import *
screensize(10000,10000)
tracer(0)
k=10
lt(90)
for i in range(9):
    fd(17*k)
    lt(90)
    fd(8*k)
    lt(90)
    fd(17*k)
up()
lt(90)
fd(3*k)
rt(90)
fd(5*k)
lt(90)
down()
for i in range(4):
    fd(97*k)
    rt(90)
    fd(132*k)
    rt(90)
up()
for x in range(-30,30):
    for y in range(-30,30):
        dot(4,'red')
        goto(x*k,y*k)
update()
done()
