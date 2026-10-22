from turtle import *
screensize(10000,10000)
tracer(0)
k=10
lt(90)
for i in range(3):
    fd(39*k)
    rt(90)
    fd(48*k)
    rt(90)
up()
fd(27*k)
right(90)
fd(24*k)
lt(90)
down()
for i in range(3):
    fd(29*k)
    rt(90)
    bk(18*k)
    rt(90)
up()
for x in range(24,43):
    for y in range(0,13):
        dot(4,'red')
        goto(x*k,y*k)
update()
done()
print(39*48+29*18-((42-24)*12))
#