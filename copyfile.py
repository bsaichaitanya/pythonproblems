from sys import argv
from os.path import exists
script , from_file , to_file = argv

in_file = open(from_file)

indata = in_file.read()

print(f"the input file {len(indata)} bytes long")

print(f"does the output file exists ? {exists(to_file)}")

print("Ready , hit return to continue. Ctrl-c to abort")

input("?")

outfile = open(to_file,'w')

outfile.write(indata)

print("Alright,done")

outfile.close()
in_file.close()

