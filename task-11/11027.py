from math import log2,ceil
N=52+458+10
i=ceil(log2(N))
for l in range(1,10000):
    I=ceil(l*i/8)
    if I*862<=276*2**10:
        print(l)