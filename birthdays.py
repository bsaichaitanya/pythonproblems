# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}


# while True:
# 	print('type the name of your friend for their bday:leave blank to exit')
# 	name = input()
# 	if name == '':
# 		break

# 	if name in birthdays:
# 		print('Birthday of your friend is on' + birthdays[name])

# 	else:

# 		print('enter the birthday of your friend')

# 		birthday = input()

# 		birthdays[name] = birthday

# 		print('birthday of' + name + 'is on ' + birthdays[name])



birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
        print('Enter a name: (blank to quit)')
        name = input()
        if name == '':
           break
        if name in birthdays:
        	print(birthdays[name] + ' is the birthday of ' + name)
        else:
           print('I do not have birthday information for ' + name)
           print('What is their birthday?')
           bday = input()
           birthdays[name] = bday
           print('Birthday database updated.')


