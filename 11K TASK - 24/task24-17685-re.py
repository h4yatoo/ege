from re import finditer
with open(r'./files/24_17685.txt')as f:
    data=f.readline()
num=r'([1-9][0-9]*|0)'
zero=rf'({num}\*)*0(\*{num})*'
pattern=rf'{zero}(\+{zero})*'
matches=[match.group() for match in finditer(pattern,data)]
print(len(max(matches,key=len)))