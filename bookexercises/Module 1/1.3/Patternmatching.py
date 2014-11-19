# Pattern matching problem
# Find all occurences of a pattern in a string
#  Input: two strings, pattern and genome
#  output: All starting positions where Pattern appears as a substring of genome

input=str(raw_input("What is the name of the file name holding the genome?"))

f= open(input,'r')
data=f.read()
f.close()

def PatternMatch(Pattern,Genome):
	i = 0
	positions=[]
	while i < len(Genome):
		if Genome[i:i+len(Pattern)]==Pattern:
			positions.append(i)
		i+=1
	return positions

result=str(PatternMatch("ATGATCAAG", data))

result = map(str,result)
result = " ".join(result)
z = open("vcpositions.txt",'w')
z.write(result)
z.close()