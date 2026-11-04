from turtle import *
screensize(10000,10000)
tracer(0)
k=10
lt(90)
rt(90)
for i in range(7):
    rt(45)
    fd(11*k)
    rt(45)
up()
for x in range(-10,10):
    for y in range(-17,10):
        dot(4, 'red')
        goto(x*k,y*k)
update()
done()
print(113)