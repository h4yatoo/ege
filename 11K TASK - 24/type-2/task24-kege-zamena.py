with open(r'../files/24_2942.txt') as f:
    s = f.readline()
s=(s.replace('AB','*').replace('AC','*')
   .replace('A',' ').replace('B',' ')
   .replace('C',' '))
print(max(len(x) for x in s.split()))
