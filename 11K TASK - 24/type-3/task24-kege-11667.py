# with open(r'../files/24_11667.txt') as f:
#     s = f.readline()
# s=s.replace('INFINITY','I NFINITY')
# s = s.split(' ')
# ans = 0
# for i in range(len(s) - 1000):
#     line = ''.join(s[i:i + 1001])
#     ans = max(ans, len(line))
# print(ans+6)

with open(r'../files/24_11667.txt') as f:
    s = f.readline()
l=r=cnt=ans=0
len_data=len(s)
while r<len_data:
    if cnt<=1000:
        if s[r:r+8]=='INFINITY':
            cnt+=1
        r+=1
    else:
        if s[l:l+8]=='INFINITY':
            cnt-=1
        l+=1
    ans=max(ans,r-l+6)
print(ans)

