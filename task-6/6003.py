from turtle import *
screensize(10000,10000)
k=10
tracer(0)
lt(90)
for i in range(2):
    fd(10*k)
    rt(90)
    fd(20*k)
    rt(90)
up()
fd(3*k)
rt(90)
fd(7*k)
lt(90)
down()
for i in range(2):
    fd(70*k)
    rt(90)
    fd(90*k)
    rt(90)
up()
for x in range(7, 21):
    for y in range(3, 11):
        teleport(x * k, y * k)
        dot(4,'red')

update()
done()
print((21-7)*(11-3))

