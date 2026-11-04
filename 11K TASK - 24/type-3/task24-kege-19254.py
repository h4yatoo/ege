# with open(r'../files/24_19254.txt')as f:
#     s=f.readline()
# l=max_len=cnt=0
# for r in range(len(s)-3):
#     if s[r:r+4]=='FSRQ':
#         cnt+=1
#     while cnt>80:
#         if s[l:l+4]=='FSRQ':
#             cnt-=1
#         l+=1
#     if cnt==80:
#         max_len=max(max_len,r-l+4)
# print(max_len)
#
# with open(r'../files/24_19254.txt')as f:
#     s=f.readline()
# s=s.replace('FSRQ','F SRQ').split(' ')
# ans=0
# for i in range(len(s)-80):
#     line=''.join(s[i:i+81])
#     ans=max(ans,len(line))
# print(ans+2)















