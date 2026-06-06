# пример задач
# data='ABCAAABACACAB'
# data = data.replace('AB','A B')
# data = data.split()
# answer = max(data, key=len)
# print(data,len(answer))



#24.01

# способ 1
# with open('../files/2401.txt') as f:
#     s = f.readline()
#     s=s.replace('ad', 'a d').replace('da', 'd a')
#     print(max(len(x) for x in s.split()))

# # способ 2
# with open('../files/2401.txt') as f:
#     s = f.readline()
# cur=1
# max_len=0
# for i in range(len(s)-1):
#     if s[i]+s[i+1] in('ad','da'):
#         cur=1
#     else:
#         cur+=1
#     max_len=max(max_len,cur)
# print(max_len)



#1 REPLACE dz
with open('../files/1873.txt') as f:
    s=f.readline()
s=s.replace('PR','P R')
s=s.replace('RP','R P')
print(max(len(x) for x in s.split()))

#COUNTER
with open('../files/1873.txt') as f:
    s = f.readline()
cur = 1
max_len = 1
for i in range(len(s) - 1):
    if s[i] + s[i + 1] in ('RP', 'PR'):
        cur = 1
    else:
        cur += 1
    max_len = max(max_len, cur)
print(max_len)


#2 REPLACE
with open('../files/2410.txt') as f:
    s = f.readline()
s=s.replace('00', '0 0')
print(max(len(x) for x in s.split()))

#COUNTER
with open('../files/2410.txt') as f:
    s = f.readline()
cur = 1
max_len = 1
for i in range(len(s) - 1):
    if s[i] + s[i + 1] == '00':
        cur = 1
    else:
        cur += 1
    max_len = max(max_len, cur)
print(max_len)



