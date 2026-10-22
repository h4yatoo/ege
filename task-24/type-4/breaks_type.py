# with open('../files/2403.txt') as f:
#     data=f.readline()
# k=160
# breaks=[0]
# max_len=0
# for i in range(len(data)-1):
#     if data[i]+data[i+1]=='CD':
#         breaks.append(i)
# breaks.append(len(data)-1)
# for i in range(1,len(breaks)-k):
#     max_len=max(max_len,breaks[i+k]-breaks[i-1])
# print(max_len)
