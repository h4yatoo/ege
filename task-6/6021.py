from turtle import *
tracer(0)
screensize(10000,10000)
k=10
lt(90)
for i in range(3):
    fd(7*k)
    rt(90)
    fd(12*k)
    rt(90)
up()
fd(4*k)
rt(90)
fd(6*k)
lt(90)
down()
for i in range(4):
    fd(83*k)
    rt(90)
    fd(77*k)
    rt(90)
up()
for x in range(0, 7):
    for y in range(0, 4):
        teleport(x*k, y*k)
        dot(4, 'red')
update()
done()
print(8*13+84*78-7*4)
