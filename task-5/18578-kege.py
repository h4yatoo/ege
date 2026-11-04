from string import printable as alph
def convert2(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1] if res else '0'
ans=0
for n in range(1,10000):
    n4=convert2(n,4)
    if n%4==0:
        r4='2'+n4+'03'
    else:
        a=(n%4)*5
        r4=n4+convert2(a,4)
    r=int(r4,4)
    if r<=567:
        ans=max(ans,n)
print(ans)
