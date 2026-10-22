with open(r'../files/24_10105.txt') as f:
     s=f.readline()
s=s.split('T')
ans=0
for i in range(len(s)-100):
    line='T'.join(s[i:i+101])
    ans=max(ans,len(line))
print(ans)