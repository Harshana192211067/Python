b=int(input("Enter number: "))
a=b
order=len(str(a))
sum=0
while(a!=0):
    digit=a%10
    sum+=digit**order 
    a=a//10
if(sum==b):
    print("armstromg num")
else:
    print("not")

      
      
