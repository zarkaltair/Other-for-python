#Fibonacci Sequence

# 1, 1, 2, 3, 5, 8, 13...

# an example with 1 to 20

fibonacciList = [0, 1]
key = 0
actualResult = 1
print(actualResult)
for f in range(0, 11):
	actualResult = fibonacciList[key] + fibonacciList[key + 1]
	print(actualResult, end = ', ')
	fibonacciList.append(actualResult)
	key += 1
print(fibonacciList)


# print('\n\n')
# print(' ' * 19, '*')
# key = 18
# for f in range(3, 21, 2):
# 	print(' ' * key, '*' * f)
# 	key -= 1
# key2 = 9
# for x in range(21, 1, -2):
# 	print(' ' * key2, '*' * x)
# 	key2 += 1
# print(' ' * 19, '*')

# def factorial(number):
# 	number = int(input('Give me a number: '))
# 	total = 1
# 	if number == 0 or number == 1:
# 		print('Factorial of', number, '= 1')
# 	else:
# 		for f in range(1, number + 1):
# 			total *= f
# 		print('Factorial of', number, '=', total)

# # armstrong Number questioning

# import math

# while True:
# 	number = input('Give me a number: ')
# 	exponential = len(number)
# 	total = 0
# 	for fuck in number:
# 		fuck = int(fuck)
# 		total += pow(fuck, exponential)
# 		print('Number:', number, 'Total:', total)
# 	if total == int(number):
# 		print('It is an armstrong number.')
# 	else:
# 		print('It is not an armstrong number.')