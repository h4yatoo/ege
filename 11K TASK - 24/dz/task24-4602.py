from re import finditer
with open(r'../files/24_4602.txt')as f:
    data=f.readline()
pattern=r'([B-D][AO])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches,key=len))//2)