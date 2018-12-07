# Python 3: Fibonacci series up to n
def fib( n ):
	a, b = 0, 1
	while a < n:
		print( a, end = ' ' )
		a, b = b, a + b
	print()
fib( 100 )

# Ввчисление числа е
def exp( z ):
	for x in range( 1, z ):
		y = ( 1 + 1/x ) ** x
		print( round( y, 5 ) )
exp( 10 )

x = 500000
y = ( 1 + 1/x ) ** x
print( round( y, 5 ) )