# with open('../files/2404.txt.txt') as f:
#     s=f

# data='TTTTZYWTTT'
# l=0
# cnt=0
# max_len=0
# k=5
# for r in range(len(data)):
#     if data[r]=='T':
#         cnt+=1
#     while cnt > k:
#         if data[l]=='T':
#             cnt-=1
#         l+=1
#     if cnt==5:
#         max_len=max(max_len,r-l+1)
# print(max_len)


# with open('../files/2425.txt') as f:
#     s = f.readline()
# l = 0
# cnt = 0
# ans = 0
# for r in range(len(s)):
#     if s[r] == 'A':
#         cnt += 1
#     while cnt > 3:
#         if s[l] == 'A':
#             cnt -= 1
#         l += 1
#     ans = max(ans, r - l + 1)
#
# print(ans)


# data='CDCDDCCDDCCDCDCDCD'

# l=max_len=i=0
# k=3
# cnt=0
#
# for r in range(len(data)-1):
#     if data[i]+data[i+1]=='CD':
#         cnt+=1
#     while cnt>k:
#         if data[l]+data[l+1]=='CD':
#             cnt-=1
#         l+=1
#     if cnt==k:
#         max_len=max(max_len,r-l+2)
# print(max_len)


with open('../files/2407.txt') as f:
    s=f.readline()
k=80
l=cnt=max_len=0
for r in range(len(s)-3):
    if s[r:r+4]=='FSRQ':
        cnt+=1
    while cnt>k:
        if s[l:l+4]=='FSRQ':
            cnt-=1
        l+=1
    if cnt==k:
        max_len=max(max_len,r-l+4)
print(max_len)