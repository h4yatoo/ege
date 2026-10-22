from turtle import *
screensize(10000,10000)
tracer(0)
k=10
lt(90)
for i in range(9):
    fd(22*k)
    rt(90)
    fd(6*k)
    rt(90)
up()
fd(1*k)
rt(90)
fd(5*k)
lt(90)
down()
for i in range(9):
    fd(53*k)
    rt(90)
    fd(75*k)
    rt(90)
up()
for x in range(0,2):
    for y in range(0,22):
        dot(4, 'red')
        goto(x*k,y*k)
update()
done()
print(2*22)
