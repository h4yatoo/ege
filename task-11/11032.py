from math import log2,ceil
N=52+963+10
i=ceil(log2(N))
for l in range(1,10000):

    I=ceil(l*i/8)
    if I*2000<=693*2**10:
        print(l)

