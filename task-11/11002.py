from math import log2,ceil
N=10+1700
l=252
i=ceil(log2(N))
I = ceil(l* i / 8)
print((I*2048)//2**10)
