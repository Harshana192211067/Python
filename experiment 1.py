l = []
b = int(input("First list size:"))
if(b>50):
        print("Out of range")
else:
        for i in range(0, b):
                a = int(input())
                l.append(a) 
l1 = []
b1 = int(input("First list size:"))
if(b1>50):
   print("Out of range")
else:
        for i in range(0, b1):
                a1 = int(input())
                l1.append(a1)
print("First list is: ",l)
print("Second list is: ",l1)
s=l+l1
s.sort()
if(len(l)>50):
        print("out of range")
else:
        print(s)

