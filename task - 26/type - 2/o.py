with open('../files/2603.txt') as f:
    n,s=map(int,f.readline().split())
    data=[]
    for line in f:
        parts=list(map(int,line.split()))
        candidate={'id':parts[0],'a':parts[1],'b':parts[2],'c':parts[3],'sob':parts[4]}
        candidate['result']=candidate['a']+candidate['b']+candidate['c']
        data.append(candidate)
data=sorted(data,key=lambda x:(x['result'],x['sob'],x['id']),reverse=True)
half_pass_mark=data[s]['result']
answer_2=0
for candidate in data:
    if candidate['result']>half_pass_mark:
        answer_1=candidate['id']
    if candidate['result']==half_pass_mark:
        answer_2+=1
print(answer_1,answer_2)