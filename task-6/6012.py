from turtle import *
screensize(10000,10000)
k=10
tracer(0)
lt(90)
for i in range(2):
    fd(13*k)
    rt(90)
    fd(20*k)
    rt(90)
up()
fd(8*k)
rt(90)
bk(3*k)
lt(90)
down()
for i in range(2):
    fd(16*k)
    rt(90)
    fd(8*k)
    rt(90)
up()
for x in range(0, 6):
    for y in range(8, 14):
        teleport(x*k,y*k)
        dot(4,'red')
update()
done()
print(17*9+14*21-(6*(14-8)))
