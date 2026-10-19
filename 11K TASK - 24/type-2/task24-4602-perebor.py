with open(r'../files/24_4602.txt') as f:
    s = f.readline()
max_len=cur=i = 0
len_s=len(s)-1
sog,gl='BCD','AO'

while i < len_s:
    if s[i] in sog and s[i+1] in gl:
        cur+=1
        i+=2
        max_len=max(max_len,cur)
    else:
        cur=0
        i+=1
print(max_len)