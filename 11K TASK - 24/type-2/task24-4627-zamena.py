with open(r'../files/24_4627.txt') as f:
    s = f.readline()
s=s.replace('NPO','*').replace('PNO','*')
for x in 'NPO':
    s=s.replace(x,' ')
print(max(len(x) for x in s.split()))