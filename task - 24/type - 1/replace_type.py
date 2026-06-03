# пример задач
# data='ABCAAABACACAB'
# data = data.replace('AB','A B')
# data = data.split()
# answer = max(data, key=len)
# print(data,len(answer))



#24.01

# способ 1
with open('../files/2401.txt') as f:
    s = f.readline()
    s=s.replace('ad', 'a d').replace('da', 'd a')
    print(max(len(x) for x in s.split()))

# способ 2
with open('../files/2401.txt') as f:
    s = f.readline()
cur=1
max_len=0
for i in range(len(s)-1):
    if s[i]+s[i+1] in('ad','da'):
        cur=1
    else:
        cur+=1
    max_len=max(max_len,cur)
print(max_len)



