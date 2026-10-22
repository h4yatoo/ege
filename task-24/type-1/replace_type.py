# пример задач
# data='ABCAAABACACAB'
# data = data.replace('AB','A B')
# data = data.split()
# answer = max(data, key=len)
# print(data,len(answer))
import string

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



#1 REPLACE dz 06.06.2026
# with open('../files/1873.txt') as f:
#     s=f.readline()
# s=s.replace('PR','P R')
# s=s.replace('RP','R P')
# print(max(len(x) for x in s.split()))

#COUNTER
# with open('../files/1873.txt') as f:
#     s = f.readline()
# cur = 1
# max_len = 1
# for i in range(len(s) - 1):
#     if s[i] + s[i + 1] in ('RP', 'PR'):
#         cur = 1
#     else:
#         cur += 1
#     max_len = max(max_len, cur)
# print(max_len)


#2 REPLACE
# with open('../files/2410.txt') as f:
#     s = f.readline()
#     while '00' in s:
#         s=s.replace('00', '0 0')
# print(max(len(x) for x in s.split()))

#COUNTER
# with open('../files/2410.txt') as f:
#     s = f.readline()
# cur = 1
# max_len = 1
# for i in range(len(s) - 1):
#     if s[i] + s[i + 1] == '00':
#         cur = 1
#     else:
#         cur += 1
#     max_len = max(max_len, cur)
# print(max_len)





#lesson 06.06.2026
# with open('../files/2417.txt') as f:
#     s=f.readline()
# s=s.replace('Q','*').replace('R','*').replace('S','*')
# while '**' in s:
#     s = s.replace('**','* *')
# print(max(len(x) for x in s.split()))



### тип3 глубже
# with open('../files/16333.txt') as f:   #REPLACE
#     s=f.readline()
# # for i in 'QRW':
# #     s = s.replace(i, '*')
# # for i in '124':
# #     s = s.replace(i, '#')
# s=s.translate(str.maketrans('QRW124', '***###'))
# while '**' in s or '##' in s:
#     s = s.replace('##','# #')
#     s = s.replace('**','* *')
# print(max(len(x) for x in s.split()))



#жадный линейный
# with open('../files/16333.txt') as f:
#     s = f.readline()
# s=s.translate(str.maketrans('QRW124', '***###'))
#
# max_len=1
# current_len=1
# for i in range(1,len(s)):
#     if s[i]!=s[i-1]:
#         current_len+=1
#         max_len=max(max_len,current_len)
#     else:
#         current_len=1
# print(max_len)



#скользящее окно
# with open('../files/16333.txt') as f:
#      s = f.readline()
# s=s.translate(str.maketrans('QRW124', '***###'))
# left=0
# max_len=0
# for right in range(1,len(s)):
#     if s[right]==s[right-1]:
#         left=right
#     current_len=right-left+1
#     max_len=max(max_len,current_len)
# print(max_len)



# with open('../files/13866.txt') as f:
#     s = f.readline()
# s=s.translate(str.maketrans('13579', '*****'))
# while "***" in s:
#     s=s.replace('***','* * *')
# print(max(len(x) for x in s.split()))




# with open('../files/13866.txt') as f:
#     s = f.readline()
# s=s.translate(str.maketrans('13579', '*****'))


# Задание 4 (2413)
# s='321154321'
# for i in range(1,len(s)):
#     if s[i] > s[i-1]:
#         s=s.replace(s[i-1]+s[i],s[i-1]+' '+s[i])
# print(max(len(x) for x in s.split()))














