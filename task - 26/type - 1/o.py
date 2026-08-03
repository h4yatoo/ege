# with open('../files/2601.txt') as f:
#     f.readline()
#     s=list(map(int,f))
# s = sorted(s,reverse=True)
# res=[s[0]]
# for i in s[1:]:
#     if res[-1] - i >=9:
#         res.append(i)
# print(len(res),res[-1])


with open('../files/2613.txt') as f:
    f.readline()
    s=list(map(int,f))
s = sorted(s,reverse=True)
res=[s[0]]
for i in s[1:]:
    if res[-1] - i >=7:
        res.append(i)
print(len(res),s[-1])
