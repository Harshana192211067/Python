def perfectn(s,e):
    for i in range(s,e+1):
        if(i**0.5 == int(i**0.5)):
            print(i)
s=int(input())
e=int(input())
perfectn(s,e)
