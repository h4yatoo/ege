# with open('../files/2432.txt') as f:
#     s=f.readline()
# cnf=l=max_len=cnt_even=0
# k=76
# even='02468'
#
# for r in range(len(s)):
#     if s[r]=='F':
#         cnf+=1
#     if s[r] in even:
#         cnt_even+=1
#     while cnt_even>1 or cnf>k:
#         if s[l]=='F':
#             cnf-=1
#         if s[l] in even:
#             cnt_even-=1
#         l+=1
#     if cnf==k and cnt_even==1 and s[l] in even:
#         max_len=max(max_len,r-l+1)
# print(max_len)



# with open('../files/2431.txt') as f:
#     s=f.readline()
# k=35
# odds='13579'
# l=max_len=cns=cnodds=0
# for r in range(len(s)):
#     if s[r]=='S':
#         cns+=1
#     if s[r] in odds:
#         cnodds+=1
#     while cns>1 or cnodds>k:
#         if s[l]=='S':
#             cns-=1
#         if s[l] in odds:
#             cnodds-=1
#         l+=1
#     while l<=r and s[l]!='S':
#         if s[l] in odds:
#             cnodds-=1
#         l+=1
#     if cns==1 and cnodds==k and s[l]=='S':
#         max_len=max(max_len,r-l+1)
# print(max_len)

# with open('../files/2428.txt') as f:
#     s=f.readline()
# l=cny=cnt=max_len=0
# for r in range(len(s)):
#     if s[r]

# with open('../files/2433.txt') as f:
#     s=f.readline()
# l=cnw=cnt=0
# min_len=10**10
# for r in range(len(s)):
#     if s[r]=='W':
#         cnw+=1
#     if r>=3 and s[r-3:r+1]=='2025':
#         cnt+=1
#     while cnw>90:
#         if s[l]=='W':
#             cnw-=1
#         if l<=r - 3 and s[l:l+4]=='2025':
#             cnt-=1
#         l+=1
# while cnw==90 and cnt>=110:
#     min_len = min(min_len, r - l + 1)
#     if s[l]=='W':
#         cnw-=1
#     if s[l:l+4]=='2025':
#         cnt-=1
#     l+=1
#
# print(min_len)

# with open('../files/2433.txt') as f:
#     data=f.readline()
# min_len=10**10
# left=cnt_w=cnt_2025=0
# for right in range(len(data)):
#     if data[right]=='W':
#         cnt_w+=1
#     if right>=3 and data[right-3:right+1]=='2025':
#         cnt_2025+=1
#     while cnt_w>90:
#         if data[left]=='W':
#             cnt_w-=1
#         if left<=right-3 and data[left:left+4]=='2025':
#             cnt_2025-=1
#         left+=1
#     if cnt_w==90 and cnt_2025>=110:
#         while cnt_w==90 and cnt_2025>=110:
#             min_len=min(min_len,right-left+1)
#             if data[left]=='W':
#                 break
#             if left<=right-3 and data[left:left+4]=='2025':
#                 cnt_2025-=1
#             left+=1
# print(min_len)

with open('../files/26549.txt') as f:
     data=f.readline()
left=cnt_y=cnt_2025=max_len=0
for right in range(len(data)):
    if data[right]=='Y':
        cnt_y+=1
    if right >= 3 and data[right - 3:right + 1]=='2025':
         cnt_2025+=1
    while cnt_2025>50:
        if left<=right-3 and data[left:left+4]=='2025':
             cnt_2025-=1
        if data[left]=='Y':
            cnt_y-=1
        left+=1
    if cnt_y>=140 and cnt_2025==50 and data[right - 3:right + 1]=='2025':
        max_len=max(max_len,right-left+1)
print(max_len)




