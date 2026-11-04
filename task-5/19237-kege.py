from string import printable as alph
def convert2(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1] if res else '0'
ans=[]
for n in range(1,1000):
    n3=convert2(n,3)
    if n%3==0:
        n3=n3+n3[-2:]
    else:
        a=sum(int(i) for i in n3)
        n3=n3+convert2(a,3)
    r=int(n3,3)
    if r>220 and r%2==0:
        ans.append(r)
print(min(ans))

