

number = int(input("please enter any number"))

if number>1:
	for i in range(2,number):
		if (number % i) == 0:
			print('number is not prime')
			break
	
	else:
		print('it is a prime')

else:
	print('neagtive numbers or 1 is always a prime number')


