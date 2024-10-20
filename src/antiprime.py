## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main(x) :
	sum1 = 0
	sum2 = 0
	i = 1
	y = x - 1

	while (i <= x):
		if x % i == 0:
			sum1 = sum1 + 1
		i = i + 1

	while y >= 1:
		i = 1
		while i <= y:
			if y % i == 0:
				sum2 = sum2 + 1
			i = i + 1

		if sum2 >= sum1:
			return ('not anti-prime')

		else: 
			y = y - 1
			sum2 = 0

	if sum2 < sum1:
		return ('anti-prime')

if __name__ == "__main__" :
	import sys
	x = int (sys.argv [1])
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main(x))
