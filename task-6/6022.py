from turtle import *
tracer(0)
screensize(10000,10000)
k=10
lt(90)
for i in range(10):
    fd(22*k)
    rt(90)
    fd(16*k)
    rt(90)
up()
fd(1*k)
rt(90)
fd(1*k)
lt(90)
down()
for i in range(10):
    fd(72*k)
    rt(90)
    fd(79*k)
    rt(90)
up()
for x in range(1, 17):
    for y in range(1, 23):
        teleport(x*k, y*k)
        dot(4, 'red')
update()
done()
print(2*(15+21))
