with open(r'../files/24_4602.txt') as f:
    s = f.readline()
for x in 'BCD':
    for y in 'AO':
        s=s.replace(x+y,'*')
for x in 'ABCDO':
    s=s.replace(x,' ')
print(max(len(x) for x in s.split()))
