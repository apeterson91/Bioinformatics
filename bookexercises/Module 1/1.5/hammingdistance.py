## Given two strings s and t of equal length
## find the hamming distance, defined as the minimum # of substitutions
## needed to be made to make one string equal to the other

def find_Ham(stringone,stringtwo):
	count = 0
	for i,k in zip(stringone,stringtwo):
		if i!=k:
			count+=1
	return count

strone = str(raw_input("What is the First String"))
strtwo = str(raw_input("What is the Second String"))

print find_Ham(strone,strtwo)