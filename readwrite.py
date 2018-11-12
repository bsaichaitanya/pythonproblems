from sys import argv


script,filename = argv


print("we are going to erase {filename}")

print("If you dont that,hit Ctr^C")

print("if you do want that hit Return")

input("?")


print("opening the file.......")

target = open(filename,'w')

print("Truncating the file")

target.truncate()

print("now i am going to ask you for 3 lines")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("I'm going to write these lines to the file")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print("And finally we close it")

target.close()



