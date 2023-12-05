a1=input()
a=str(a1)
if len(a)==8 or len(a)==10:
    b= a1.isnumeric()
    if b== True:      
        print("valid")
    else:
        print(False)
