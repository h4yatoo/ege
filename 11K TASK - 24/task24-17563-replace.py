with open(r'./files/24_17563.txt')as f:
    data=f.readline()
s=[]
data=data.replace('-','*')
data=data.replace('**',' ')
for i in '89':
    data=data.replace(i,'7')
data=data.replace('*0',' ')
while ' 0' in data: data=data.replace(' 0',' ')
data=data.split()
for i in data:
    i=i.strip('*')
    s.append(i)
print(len(max(s,key=len)))


