from math import log2,ceil
for l in range(1,1000):
    n=70+10
    i=ceil(log2(n))
    I=ceil(l*i/8)
    if I*1234567>24*2**20:
        print(l)
        break
