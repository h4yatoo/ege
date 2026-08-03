# with open('../files/26549.txt') as f:
#     s=f.readline()
# max_len=0
# for i in range(len(s)):
#     cny = cnt2025 = 0
#     for j in range(i,len(s)):
#         if s[j]=='Y':
#             cny+=1
#         if j>=i+3 and s[j-3:j+1]=='2025':
#             cnt2025+=1
#         if cnt2025>50:
#             break
#         if cnt2025==50 and cny>=140:
#             max_len=max(max_len,j-i+1)
# print(max_len)


with open('../files/26549.txt') as f:
    s=f.readline()
max_len=0
for i in range(len(s)-1,-1,-1):
    cny = cnt2025 = 0
    if s[i-3:i+1]=='2025':
        for j in range(i,-1,-1):
            if s[j]=='Y':
                cny+=1
            elif s[j-3:j+1]=='2025':
                cnt2025+=1
            else:
                continue
            if cnt2025>50:
                break
            if cnt2025==50 and cny>=140:
                max_len=max(max_len,i-j+1)
print(max_len)
