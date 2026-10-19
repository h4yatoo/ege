with open(r'../files/24_2942.txt') as f:
    s = f.readline()
max_len = 0
for i in range(len(s) - 1):
    cur = 0
    while i + 1 < len(s) and s[i:i + 2] in ('AB', 'AC'):
        cur += 1
        i += 2

    max_len = max(max_len, cur)
print(max_len)