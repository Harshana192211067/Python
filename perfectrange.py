perfect=[]
for i in range(1,101):
    sum=0
    for j in range(1,i):
        if(i%j==0):
            sum=sum+j
    if(sum==i):
        perfect.append(i)
print(perfect)
