#tech numbers has even number of digits.if no.is split into 2 halves,
#then square of sum of these halves is
#equal to number itself.write pyython program to generate
#and print all 4 digit tech numbers.

for a in range(1000,10000):
    b=str(a)
    if len(b) % 2 == 0:
        m=len(b)//2
        n=int(b[:m])
        s=int(b[m:])
        if(n+s)**2==a:
            print(a)
    
        
