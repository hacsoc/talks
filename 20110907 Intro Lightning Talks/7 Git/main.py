from util import fib, mean
import sys

def main(max_fib=30):
	if max_fib > 30:
		raise Exception

	for i in range(0, max_fib):
		print fib(i+90)

	print mean([0,2,4,5,6,7,5,9])


if __name__ == "__main__":
	main(int(sys.argv[1]))