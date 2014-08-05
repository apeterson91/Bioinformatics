## Given <= 10 DNA strings in FASTA format (of length at most 1kbp each)
## Return the ID of the string having the highest GC-content, follwed by the 
#GC content of that string. abs. error <=0.001

# def highest_GC_ID(filename):

import string
from Bio import Seq

def highest_GC(filename):
	with open(filename,"r") as textfile:
		test=textfile.read()
	return test

input = "test.txt" #str(raw_input("What is the name of the textfile?"))

print highest_GC(input)