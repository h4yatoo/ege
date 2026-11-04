from string import printable as alph
def convert2(num,sys):
    res=''
    while num:
        res+=alph[num%sys]
        num=num//sys
    return res[::-1] if res else '0'
res=[]
for n in range(11,10000):
    n3=convert2(n,3)
    a=n3.count('0')+n3.count('2')
    b=n3.count('1')
    if a>b:
        n3='22'+n3
    else:
        n3='11'+n3
    r=int(n3,3)
    if r >100:
        res.append(r)
print(min(res))
222 28 120 30 2842 8