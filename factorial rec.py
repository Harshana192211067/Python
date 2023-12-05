# Python 3 program to find 
# factorial of given number
def factorial(n):
	if n < 0:
		print("NOt exist")
	elif n == 0 or n == 1:
		return 1
	else:
		fact = 1
		while(n > 1):
			fact *= n
			n -= 1
		return fact

# Driver Code
num = -1
print("Factorial of",num,"is",factorial(num))

