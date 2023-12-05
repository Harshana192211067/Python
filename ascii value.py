c=input("Enter any STRING : ")
l=len(c)
for i in c:
    if i==" ":
        print("ASCII value of ' ' is ",ord(i))
    else:
        print("ASCII value of ",i," is ",ord(i))
