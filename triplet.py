a=int(input())
for i in range(1,a+1):
    for j in range(1,i):
        for k in range(1,j):
            if i*i==j*j+k*k:
                print(k,j,i)
