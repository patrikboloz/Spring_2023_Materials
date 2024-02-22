def bad_fibonacci(n):
	"""Return the nth Fibonacci number"""
	if n <=1:
		return n
	else:
		return bad_fibonacci(n-2) + bad_fibonacci(n-1)

def good_fibonacci(n):
	"""Return pair of Fibonacci numbers, F(n) and F(n-1)"""
	if n <=1:
		return (n, 0)
	else:
		(a,b) = good_fibonacci(n-1)
		return (a+b, a)


print(good_fibonacci(800))

def infinite(n): #example of an infinite recursion
    return infinite(n)


infinite(50)
	