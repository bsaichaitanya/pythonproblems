types_of_people = 10 # This will assign 10 to the variable types_of_people
x = f"There are {types_of_people} of people"  # f used before string gives string formatting and load variable types_of_people

binary = "binary"
do_not = "dont"

y = f"Those who know {binary} and those who {do_not}"


print(x)
print(y)


print(f"I said :{x}") # string x is loaded 
print(f"I also said: {y}")# string y is loaded

hilarious = False
joke_evaluation = "Isnt that joke so funny?! {}"


print(joke_evaluation.format(hilarious)) # joke_evaluation and hilarious are loaded

w = "This is the left side of......"
e = "a string with right side"

print(w + e) # string w and string e are added together


