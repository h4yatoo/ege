with open(r'../files/24_9753.txt') as f:
    s=f.readline()
max_len=cny=l=0
for r in range(len(s)):
    if s[r]=='Y':
        cny+=1
    while cny>150:
        if s[l]=='Y':
            cny-=1
        l+=1
    if cny==150:
        max_len=max(max_len,r-l+1)
print(max_len)


# with open(r'../files/24_9753.txt') as f:
#      s=f.readline()
# s=s.split('Y')
# ans=0
# for i in range(len(s)-150):
#     line='Y'.join(s[i:i+151])
#     ans=max(ans,len(line))
# print(ans)