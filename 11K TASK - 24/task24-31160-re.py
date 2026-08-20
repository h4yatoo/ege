from re import finditer
with open(r'./files/24_31160.txt')as f:
    data=f.readline()
pattern=r'M{,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})'
matches=[match.group() for match in finditer(pattern,data)]
max_len=len(max(matches,key=len))
longest=[match for match in matches if len(match)==max_len]
numbers={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1,'CM':900,'CD':400,'XC':90,'XL':40,'IX':9,'IV':4}

ans=10000000
for num in longest:
    summ=0
    flag=0
    for d1,d2 in zip(num,num[1:]):
        if flag:
            flag=0
            continue
        if d1+d2 in numbers:
            summ+=numbers[d1+d2]
            flag=1
        else:
            summ+=numbers[d1]
    if not flag:
        summ+=numbers[num[-1]]
    ans=min(ans,summ)
print(ans)