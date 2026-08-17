from re import finditer
with open(r'../files/24_7600.txt')as f:
    data=f.readline()
pattern= r'[^QRS]*(Q+[^QRS]*)+|[^QRS]*(R+[^QRS]*)+|[^QRS]*(S+[^QRS]*)+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches,key=len)))