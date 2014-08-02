### Rosalind String Exercises


### Finding the complement of the given DNA String
def find_complement(filename):
	f = open(filename,"r")

	example= f.read()

	revexample=example[::-1]
	print revexample
	result= []
	for i in revexample:
		if i=="A":
			result.append("T")
		elif i=="T":
			result.append("A")
		elif i=="G":
			result.append("C")
		elif i=="C":
			result.append("G")

	result= "".join(result)
	f.close()
	
	return result

question = str(raw_input("What is the filename?"))
print find_complement(question)