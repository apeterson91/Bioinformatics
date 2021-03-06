

#implement PatternCount: Given a pattern and a string, find out how many times that 
# pattern occurs in the string

import random
import string
import operator

string = "GCTTCTATCCTTCTATCTTCTATCATCGTGAGACCTTCTATCACTTCTATTACTTCTATCTTCTATCCTTCTATCACTTCCCTTCTATCTTCTATCTTCTATAACCTTCTATCTTCTATTCTTCTATCTAACCCCTTCTATCTTCTATCGGCAACTTCTATTTAGACTTCTATATCCCTTTCCCTTCTATCTGTCCCCTTCTATCCTTCTATAAAGGCCTTCTATACTTCTATTGCTTCTATCTTCTATTTACACTTCTATTAGCTTCTATGGCTTCTATCTTACAGGGCGGCCTTCTATATTGTCTTCTATCTTCTATCTTCTATTACTTCTATAACCGCCCACTTCTATCTTCTATACCTTCTATTGCTTCTATTACTTCTATCTCTTCTATGCTTCTATGCAACTTCTATACCTTCTATTTCTTCTATGCTTCTATCCATGCCTTCTATTCCGTTTATAGGTTCTTCTATCTTCTATCTTCTATTTTTAACCTTCTATGCCCACCTTCTATCTTCTATTTCTTCTATACTTCTATAGGTCTTCTATACTTCTATAATCTTCTATCTTCTATCTTCTATCTTCTATTATCTTCTATAAGCTTCTATACTTCTATCAGCTTCTATGTCTTCTATACTTGTAGTACATCCTTCTATCTTCTATCTTCTATGTCTTCTATCTTTCTTCTATTCCCCTTCTATGAGGCTTCTATCTTCTATCTTCTATTCTTCTATCCCCTTCTATCACTTGGTAGCTTCTATATCTTCTATACCTTCTATAGCGCTTCTATTCTTCTATTGTCTTCTATCTTCTATATCTTCTATTTCCCTTCTATCTTCTATCTCCCGTCAGTACGGTACACTTCTATGCTTCTATTACTTCTATCTTCTATTCTTCTATTCTTCTATCGCTTCTATACTTCTATCTCTTCTATTGTGCTTCTATGGCCTTCTATTAATAGGTCTTCTATCAGCCTTCTATCTTCTATTGCTTCTATACTTCTATATCTTCTATCAAAACTTCTATAATCGTGTCCTTCTATCTTCTAT"

#counts the number of times a pattern occurs in a string 
def PatternCount(text, pattern):
 	patlength=len(pattern)
 	txtlength=len(text)
 	count = 0 
 	i=0
 	while i < txtlength:
 		if text[i:i+patlength]==pattern:
 			count+=1
 		i+=1
 	return count

# print PatternCount(string,"CTTCTATCT") Test for book exercise
# PatternCount gives correct output 9/25/14


# Most frequent k-mer in Text  is if it maximizes among all k-mers. 

# FrequentWords finds the most Frequent pattern in a string, given an integer 
#that details how long the potential k-mer can be.

def FrequentWords(Text,k):
	Patterns={}
	FrequentPatterns=[]
	i=0
	while i < len(Text):
		Pattern = Text[i:i+k]
		if len(Pattern)==k:
			Patterns[Pattern]=PatternCount(Text,Pattern)
		i+=1
	maxCount=max(Patterns.values())
 	for i,k in Patterns.iteritems():
 		if k==maxCount:
 			FrequentPatterns.append(i)
 	return FrequentPatterns


Testtext= "CGAATGGTCAGTTTATGAAACTAGTCGAATGGTCTTTACTTTTTACTTGAAACTAGTTTGTTGCGGAAACTAGTTTTACTTAGTTTATTTTACTTTTTACTTCGAATGGTCTTGTTGCGGAAACTAGTAGTTTATCGAATGGTCTTTACTTTTGTTGCGAGTTTATTTGTTGCGAGTTTATAGTTTATTTGTTGCGTTGTTGCGAGTTTATTTGTTGCGTTGTTGCGTTTACTTGAAACTAGTTTGTTGCGCGAATGGTCGAAACTAGTAGTTTATCGAATGGTCCGAATGGTCAGTTTATTTTACTTGAAACTAGTTTGTTGCGGAAACTAGTAGTTTATGAAACTAGTAGTTTATTTGTTGCGGAAACTAGTAGTTTATGAAACTAGTCGAATGGTCTTGTTGCGAGTTTATGAAACTAGTTTGTTGCGCGAATGGTCTTGTTGCGAGTTTATGAAACTAGTTTTACTTAGTTTATAGTTTATTTGTTGCGTTGTTGCGGAAACTAGTTTGTTGCGGAAACTAGTAGTTTATCGAATGGTCTTGTTGCGCGAATGGTCTTGTTGCGGAAACTAGTGAAACTAGTCGAATGGTCCGAATGGTCTTGTTGCGTTTACTTAGTTTATAGTTTATTTTACTTCGAATGGTCAGTTTATGAAACTAGTCGAATGGTCTTTACTTTTGTTGCGAGTTTATTTTACTTGAAACTAGTCGAATGGTCTTTACTTAGTTTATTTGTTGCGAGTTTATGAAACTAGTTTTACTTTTGTTGCGTTTACTTTTGTTGCGAGTTTATTTGTTGCGCGAATGGTCCGAATGGTCTTGTTGCGTTGTTGCGAGTTTATGAAACTAGTGAAACTAGT"

output= FrequentWords(Testtext,14)
print output

f= open('kmeroutput.txt','w')
f.write(str(output)) 
f.close()

## Frequent words gives correct output 9/25/14

