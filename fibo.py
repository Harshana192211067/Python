n=int(input())
num1=0
num2=1
nexnum=num1+num2
print("0\n1")
count=2
while(count<n):
    count+=1
    num1=num2
    num2=nexnum
    nexnum=num1+num2
    print(nexnum)       
      
