with open(r'../files/24_4627.txt') as f:
    s = f.readline()
max_len=cur=i = 0
len_s=len(s)-2
even='NPO PNO'
while i < len_s:
    if s[i:i+3] in even:
        cur+=1
        i+=3
        max_len=max(max_len,cur)
    else:
        cur=0
        i+=1
print(max_len)
