a=[1,2,3,4,5]
s=int(input())
start=0
stop=len(a)-1
while(start<=stop):
    mid=(start+stop)//2
    if(s==a[mid]):
        print(mid+1)
        break
    elif(s<a[mid]):
        stop=mid-1
    else:
        start=mid+1
else:
    print("not found")
    
