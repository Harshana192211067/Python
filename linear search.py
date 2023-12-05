a=[]
b=int(input("Enter number of elements: "))
for i in range(0,b):
    ele=int(input())
    a.append(ele)
s=eval(input("SEarching element: "))
for i in range(0,len(a)):
    if s==a[i]:
        print(i+1)
        break
else:
  print("NOT")
