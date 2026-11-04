res=[]
for n in range(1,10000):
    n2=f'{n:b}'
    if n%3==0:
        n2=n2+n2[-3:]
    else:
        k=(n%3)*3
        n2=n2+f'{k:b}'
    r=int(n2,2)
    if r>151:
        res.append(r)
print(min(res))

