import os 
filter = []
for filepath,dir,filenames in os.walk(r'C:\Users\sai\Desktop\dosc'):
		for element in filenames:
			filter.append(element)



newstr = filter
print(len(newstr))


def jpegfilter(x):
	jpeglist =[]
	for line in x:
		if line.endswith('.jpeg') | line.endswith('.jpg') | line.endswith('.JPG'):
			jpeglist.append(line)

	return jpeglist

def pdffilter(x):
	pdflist = []
	for line in x:
		if line.endswith('.pdf'):
			pdflist.append(line)

	return pdflist

def psdfilter(x):
	psdlist = []
	for line in x:
		if line.endswith('.psd'):
			psdlist.append(line)

	return psdlist

def docfilter(x):
	doclist = []
	for line in x:
		if line.endswith('.doc'):
			doclist.append(line)

	return doclist


print("number of jpeg files-{}".format(len(jpegfilter(newstr))))
print("number of pdf files-{}".format(len(pdffilter(newstr))))
print("number of doc files-{}".format(len(docfilter(newstr))))
print("number of doc files-{}".format(len(psdfilter(newstr))))
print("Total number of files-{}".format( len(jpegfilter(newstr)) + len(pdffilter(newstr)) + len(docfilter(newstr)) + len(psdfilter(newstr))) )