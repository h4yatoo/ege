res=[]
for n in range(4,10000):
    n2=f'{n:b}'
    if n%2==0:
        r2=n2+n2[:3]
    else:
        r2='1'+n2+'01'
    r=int(r2,2)
    if r>600:
        res.append(r)
print(min(res))


