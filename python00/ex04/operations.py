import sys

def usage():
	print("Usage: python operations.py <number1> <number2>")
	print("Example:\n    python operations.py 10 3")

sys.argv.pop(0)
if len(sys.argv) == 0:
	usage()
elif len(sys.argv) == 1:
	print("InputError: not enough arguments\n")
	usage()
elif len(sys.argv) > 2:
	print("InputError: too many arguments\n")
	usage()
else:
	if sys.argv[0].isdigit() == False or sys.argv[1].isdigit() == False:
		print("InputError: only numbers\n")
		usage()
	else:
		a = int(sys.argv[0])
		b = int(sys.argv[1])
		print("Sum:         " + str(a + b))
		print("Difference:  " + str(a - b))
		print("Product:     " + str(a * b))
		if b == 0:
			print("Quotient:    ERROR (div by zero)")
		else:
			print("Quotient:    " + str(a / b))
		if b == 0:
			print("Remainder:   ERROR (modulo by zero)")
		else:
			print("Remainder:   " + str(a % b))
