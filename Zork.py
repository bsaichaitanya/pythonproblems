from sys import argv


script , username = argv


prompt ='>'

print(f"Hi {username} ,I'm the {script} script" )

print("I'd like you tu ask few questions")

print(f"Do you like me {username}")
likes = input(prompt)

print(f"Where do you live {username}")

lives = input(prompt)

print("What kind of computer do you have?")

computer = input(prompt)


print(f""" Alright so you said likes {likes} about liking me 
You live in {lives}.Not sure where That is
And you have a computer {computer}.Nice
""")

