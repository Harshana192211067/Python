n=int(input())
sum=0
temp=n
while n!=0:
    rem=n%10
    sum+=rem
    n//=10
if temp%sum==0:
    print("s")
