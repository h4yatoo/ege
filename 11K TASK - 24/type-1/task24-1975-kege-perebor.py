with open(r'../files/24_1975.txt')as f:
    s = f.readline()
cur = 1
max_len = 1
for i in range(len(s) - 1):
    if s[i] + s[i + 1] == 'PP':
        cur = 1
    else:
        cur += 1
    max_len = max(max_len, cur)
print(max_len)