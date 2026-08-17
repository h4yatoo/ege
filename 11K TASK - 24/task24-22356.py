from re import finditer
with open(r'./files/24_22356.txt')as f:
    data=f.readline()
pattern=r'[1-9AB][0-9AB]*[13579B]'
matches=[match.group() for match in finditer(pattern,data)]
ans=max(matches,key=lambda x:int(x,12))
print(data.find(ans))

