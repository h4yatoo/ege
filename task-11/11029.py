from math import log2,ceil
N=26+450+10
i=ceil(log2(N))
for l in range(1,10000):
    I=ceil(l*i/8)
    if I*708>213*2**10:
        print(l)
        break