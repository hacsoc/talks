
def fib(n):
	"""Find the nth term of the Fibonacci sequence."""
	if n < 2:
		return n
	
	return fib(n-2) + fib(n-1)

def mean(n):
	return sum(n) / len(n)
	