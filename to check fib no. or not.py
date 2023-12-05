import math
def is_perfect_square(n):
	root = int(math.sqrt(n))
	return (root * root == n)
def is_fibonacci(n):
	if n == 0:
                return True
	a, b, c = 0, 1, 1
	while c < n:
		a = b
		b = c
		c = a + b

	return c == n or is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)
m=int(input())
for i in range(1, m+1):
	if is_fibonacci(i):
		print(i, "is a Fibonacci number.")
	else:
		print(i, "is not a Fibonacci number.")
