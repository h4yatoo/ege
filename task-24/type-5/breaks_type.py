# with open('../files/2432.txt') as f:
#     s=f.readline()
# max_len=0
# k=76
# even='02468'
# breaks_1=[0]
# breaks_2=[0]
# for i in range(len(s)):
#     if s[i] in even:
#         breaks.append(i)
# breaks.append(len(s))
# for i in range(len(breaks)-1):
#     cnf=s[breaks[i]:breaks[i+1]].count('F')
#     if cnf==k:
#         max_len=max(max_len,breaks[i+1]-breaks[i])
# print(max_len)


# with open('../files/26549.txt') as f:
#     s=f.readline()
# k=50
# breaks=[]
# for i in range(len(s)):
#     if s[i:i+4]=='2025':
#         breaks.append(i)
# max_len=0
# for i in range(len(breaks)-k):
#     end=breaks[i+k]+3
#     start=breaks[i]
#     cny=0
#     for j in range(start,end):
#         if s[j]=='Y':
#             cny+=1
#         if cny>=140:
#             max_len=max(max_len,end-start)
# print(max_len)
