import sys

sys.argv.pop(0)
sys.argv.reverse()
for i in range(len(sys.argv)):
	sys.argv[i] = sys.argv[i][::-1]
	sys.argv[i] = sys.argv[i].swapcase()
	if i == len(sys.argv) - 1:
		print(sys.argv[i])
	else:
		print(sys.argv[i], end=' ')
