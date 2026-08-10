from re import finditer
with open(r'../files/24_2942.txt')as f:
    data=f.readline()
pattern=r'(A[B-C])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches,key=len))//2)