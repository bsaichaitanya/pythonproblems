
def collatz(number):
		if number % 2 == 0:
			print(number//2)
			return number//2
		elif number % 2 != 0:
			print(3 * number + 1)
			return 3 * number + 1

try:	
	number = int(input())


	while collatz !=1:
		number = collatz(number)
		if number == 1:
			break
except NameError:
	print("the number is not given")
except ValueError:
	print('lease provide a number ')
