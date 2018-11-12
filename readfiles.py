from sys import argv

script , filename = argv # takes the file name form command line and aasigns it to the filename

txt = open(filename) # opens the file given in command line arguments and returns a file object

print(f"Hers's your filename {filename}") # prints the name of file

print(txt.read()) # reads the file and prints it

print("Type the filename again:")

file_again = input('>')

txt_again = open(file_again)

print(txt_again.read())
