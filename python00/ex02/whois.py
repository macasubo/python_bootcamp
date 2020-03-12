import sys

sys.argv.pop(0)
if len(sys.argv) != 0:
	if len(sys.argv) > 1 or sys.argv[0].isdigit() == False:
		print('ERROR')
	else:
		if int(sys.argv[0]) == 0:
			print("I'm Zero.")
		elif int(sys.argv[0]) % 2 == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")
