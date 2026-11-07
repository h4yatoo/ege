# max_len=0
# for n in range(1,501):
#     n2=bin(n)[2:]
#     n2=n2[::-1]
#     r=int(n2,2)
#     if  r ==11:
#         max_len=max(max_len,n)
# print(max_len)
# print('x y z w')
# for x  in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x<=y and not(z)) or w)==False:
#                     print(x,y,z,w)

# print(21*8/7)
# print((2000*1000*25-800*700*15)*40/2**13)
# from turtle import *
# screensize(10000, 10000)
# tracer(0)
# k = 20
# lt(90)
# for i in range(6):
#     fd(33 * k)
#     rt(90)
#     fd(20 * k)
#     rt(90)
# up()
# fd(3 * k)
# rt(90)
# fd(9 * k)
# lt(90)
# down()
# for i in range(6):
#     fd(24 * k)
#     rt(90)
#     fd(25 * k)
#     rt(90)
# up()
# for x in range(10, 20):
#     for y in range(4, 27):
#         teleport(x * k, y * k)
#         dot(4, 'red')
# update()
# done()
# print((20 - 10) * (27 - 4))

# res=[]
# for n in range(1,1000):
#     n2=f'{n:b}'
#     if n2.count('1')%2==0:
#         n2='10'+n2[2:]+'0'
#     else:
#         n2 = '11' + n2[2:] + '1'
#     r=int(n2,2)
#     if r>=16:
#         res.append(n)
# print(min(res))

from string import printable as alph
def c(n,s):
    res = ''
    while n:
        res += alph[n % s]
        n //= s
    return res[::-1] if res else '0'
ans = []
for n in range(1, 1000):
    n4=c(n,4)
    a=sum(int(i) for i in n4)
    if a%2==1:
        n4='2'+n4+'0'
    else:
        n4 = n4 + n4[-2:]
    r = int(n4, 4)
    if r > 120 and r % 2 == 0:
        ans.append(r)
print(min(ans))




