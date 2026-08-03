# with open('../files/16333.txt') as f:
#       s = f.readline()
# s='AA22BX12'
# good='0123456789AB'
# even='02468A'
# max_len=0
# l=0
# for r in range(len(s)):
#     if s[r] not in good:
#         b=s[l:r]
#         if b:
#             if b[-1] in even:
#                 if len(b)==1 or b[0]!='0':
#                     max_len=max(max_len,len(b))
#         l=r+1
# b=s[l:]
# if b:
#     if b[-1] in even:
#         if len(b)==1 or b[0]!='0':
#             max_len=max(max_len,len(b))
# print(max_len)


