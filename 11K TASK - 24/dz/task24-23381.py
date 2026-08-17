from re import finditer
from string import ascii_uppercase

with open(r'../files/24_23381.txt')as f:
    data=f.readline()
pattern=  r'[02468]([A-Z])\1*[02468]'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches,key=len)))

#################################################
ans=0
for letter in ascii_uppercase:
    pattern=rf'[02468]{letter}+[02468]'
    matches = [match.group() for match in finditer(pattern, data)]
    if matches:
        ans=max(ans,len(max(matches,key=len)))
print(ans)
