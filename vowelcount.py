a=input("Enter string: ")
b=a.split()
vowels=['a','e','i','o','u','A','E','I','O','U']
for ij in b:
    count=0
    for i in range(0,len(ij)):
        if ij[i] in vowels:
            count=count+1
    print(count)
        
