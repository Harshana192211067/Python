a=1
b=100
for i in range(a,b+1):
    c=0
    for j in range(2,i):
        if(i%j==0):
            c=1
            break
if(c==0):
    print(i)


