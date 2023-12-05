a=input("enter string 1 ")
b=input("enter string 2 ")
a=a.split()
b=b.split()
l=a[:]
m=b[:]
#print(l)
for i in l:
    if i in b:
        b.remove(i)
for i in m:
    if i in a:
        a.remove(i)
#print(b)
c=' '.join(b)
d=' '.join(a)
print("First string: ",d)
print("Second  string: ",c)
