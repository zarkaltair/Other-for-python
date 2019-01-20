# Fibonacci series up to n
def fib(n):
	a, b = 0, 1
	arr = []
	x = 0
	while x < n:
		arr.append(a)
		a, b = b, a + b
		x += 1
	return arr

print(fib(15))


# Ввчисление числа е
# def exp(z):
# 	for x in range(1, z):
# 		y = (1 + 1/x) ** x
# 		print(round(y, 5))

# exp(10)


# x = 500000
# y = (1 + 1/x) ** x
# print(round(y, 5))