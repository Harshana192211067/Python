a="112"
b="336"
d1={}
d2={}
for i in a:
    if i not in d1:
        d1[i]=1
    else:
        d1[i]+=1
for i in b:
    if i not in d2:
        d2[i]=1
    else:
        d2[i]+=1
a1=[]
a2=[]
for i in d1.values():
    a1.append(i)
for i in d2.values():
    a2.append(i)
if a1==a2:
    print("Yes,it is anagram...")
else:
    print("No,it is not anagram...")
