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
    if sum(int(i) for i in n3)%2==0:
        n3='12'+n3[2:]+'0'
    else:
        n3='10'+n3[2:]+'2'
    r=int(n3,3)
    if r>105:
        ans.append(n)
print(min(ans))