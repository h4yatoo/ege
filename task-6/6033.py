from turtle import *
screensize(10000,10000)
tracer(0)
k=10
lt(90)
for i in range(2):
    fd(20*k)
    lt(270)
    fd(12*k)
    rt(90)
up()
fd(9*k)
rt(90)
fd(7*k)
lt(90)
down()
for i in range(2):
    fd(13*k)
    rt(90)
    fd(6*k)
    rt(90)
up()
for x in range(7,13):
    for y in range(9,21):
        dot(4,'red')
        goto(x*k,y*k)
update()
done()
print(13*21+14*7-(13-7)*(21-9))