ans=[]
for n in range(2,10000):
    sum_1=sum(int(i) for i in str(n) if int(i)%2==0)