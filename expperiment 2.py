n=int(input("enter size:"))
a=[]
for i in range(0,n):
    s=input(f"enter string {i+1} ")
    a.append(s)
length=0
for i in a:
    t=i.split()
    if length<len(t):
        length=len(t)
print(length)
