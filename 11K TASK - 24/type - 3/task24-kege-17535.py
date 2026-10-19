# with open(r'..\files\24_17535.txt') as f:
#     s = f.readline()
# max_len = cnt = l = 0
# for r in range(len(s)):
#     if s[r:r+2] == 'CD':
#         cnt += 1
#     while cnt > 160:
#         if s[l:l+2] == 'CD':
#             cnt -= 1
#         l += 1
#     if cnt == 160:
#         max_len = max(max_len, r - l + 2)
# print(max_len)

with open(r'..\files\24_17535.txt') as f:
    s = f.readline()