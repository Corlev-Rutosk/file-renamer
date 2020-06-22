import os

directory = r'C:\...'

FilenameList = []
NewFilenameList = []

#--------------------------------------------------------

def printout():
	print ("\n" * 2, "------OLD FILE NAMES-------", "\n")
	
	for iterable in FilenameList:
		print (iterable)		

	print ("\n", "------NEW FILE NAMES-------", "\n")

	for iterable in NewFilenameList:
		print (iterable)		

	print ("\n" * 2)

#--------------------------------------------------------

# SHIFT ALL FILES OF ONE NUMBER UP BY X
def OneShift():
	for filename in os.listdir(directory):
		if filename[:2] == digit:
			FilenameList.append(filename)
			newfilename = str(int(filename[:2]) + int(offset)) + filename[2:]
			if int(newfilename[:2]) < 10:
					newfilename = "0" + str(int(filename[:2]) + int(offset)) + filename[2:]
			NewFilenameList.append(newfilename)

	printout()

	if input("EXECUTE? y/n ")== "y":
		for filename in os.listdir(directory):
			if filename[:2] == digit:
				newfilename = str(int(filename[:2]) + int(offset)) + filename[2:]
				if int(newfilename[:2]) < 10:
					newfilename = "0" + str(int(filename[:2]) + int(offset)) + filename[2:]
				os.rename(f'{directory}\{filename}', f'{directory}\{newfilename}')

#---------------------------------------------------------	
# SHIFT ALL NUMBERS AFTER __

def AllShift():
	for filename in os.listdir(directory):
		if int(filename[:2]) >= int(digit):
			FilenameList.append(filename)
			newfilename = str(int(filename[:2]) + int(offset)) + filename[2:]
			if int(newfilename[:2]) < 10:
				newfilename = "0" + str(int(filename[:2]) + int(offset)) + filename[2:]
			NewFilenameList.append(newfilename)

	printout()
	
	if input("EXECUTE? y/n ")== "y":
		for filename in os.listdir(directory):
			if int(filename[:2]) >= int(digit):
				newfilename = str(int(filename[:2]) + int(offset)) + filename[2:]
				if int(newfilename[:2]) < 10:
					newfilename = "0" + str(int(filename[:2]) + int(offset)) + filename[2:]
				os.rename(f'{directory}\{filename}', f'{directory}\{newfilename}')

		

#----------------------------------------------------

digit = input("set start digit: ")
offset = input("set offset: ")

WhichFunction = input("All or one? [a/o]: ")

if WhichFunction == "o":
	OneShift()
elif WhichFunction == "a":
	AllShift()





