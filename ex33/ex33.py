def crateNumbers(k, numbers, increase):
	i = 0
	while i < k:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i+increase
		print "Numbers now: ",  numbers
		print "At the bottom i is %d" % i
	return numbers
from sys import argv
srcipt, k, increase = argv
numbers = []
numbers = crateNumbers(int(k), numbers, int(increase))

print "The bumbers: "
for num in numbers:
	print num
