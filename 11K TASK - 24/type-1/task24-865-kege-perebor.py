with open(r'../files/24_865.txt')as f:
    s = f.readline()
cur = 0
max_len = 1
for i in range(len(s)):
    if s[i] in ('C','F'):
        cur = 0
    else:
        cur += 1
    max_len = max(max_len, cur)
print(max_len)