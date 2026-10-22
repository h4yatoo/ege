from turtle import *
screensize(10000,10000)
k=10
tracer(0)
lt(90)
for i in range(2):
    fd(25*k)
    rt(90)
    fd(10*k)
    rt(90)
up()
fd(3*k)
lt(90)
fd(15*k)
rt(90)
down()
for i in range(2):
    fd(9*k)
    rt(90)
    fd(32*k)
    rt(90)
up()
for x in range(0, 6):
    for y in range(8, 14):
        teleport(x*k,y*k)
        dot(4,'red')
update()
done()
