from math import log2,ceil
l=248
for N in range(1,100000):
    i=ceil(log2(N))
    I=ceil(i*l/8)
    if I*75600>16*2**20:
        print(N)
        break
