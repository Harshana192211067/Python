n =int(input())
while n != 1 and n != 4:
    n = sum(int(digit) ** 2 for digit in str(n))

if n == 1:
    print(True)
else:
    print(False)

