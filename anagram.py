a=input("Enter string 1: ")
b=input("Enter string 2: ")
dic1={}
dic2={}
for i in a:
    if i not in dic1:
        dic1[i]=1
    else:
        dic1[i]=dic1+1
for i in b:
    if i not in dic2:
        dic2[i]=1
    else:
        dic2[i]=dic2+1
if dic1==dic2:
    print("Anagram")
else:
    print("not anagram")
