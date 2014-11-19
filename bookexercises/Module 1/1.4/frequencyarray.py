#Converting Patterns to Numbers and Numbers to Patterns

def SymbolToNumber(symbol):
	bases= { "A":0 , "C":1, "G":2, "T":3}
	return bases[symbol]
def NumberToSymbol(number):
	bases= {0 :"A",  1: "C", 2 :"G", 3: "T"}
	return bases[number]
	
def PatternToNumber(Pattern):
	if len(Pattern)==0:
		return 0
 	Symbol = Pattern[len(Pattern)-1:len(Pattern)]
 	Pattern = Pattern[0:len(Pattern)-1]
	return 4 * PatternToNumber(Pattern) + SymbolToNumber(Symbol)

# print PatternToNumber("ATGCAA") # Correct as of 9/28/14

def NumberToPattern(index,k):
	if k==1:
		return NumberToSymbol(index)
	quotient = index/4
	remainder = index % 4
	PrefixPattern = NumberToPattern(quotient,k-1)
	symbol= NumberToSymbol(remainder)
	return PrefixPattern + symbol

def ComputingFrequencies(Text,k):
	FrequencyArray=[]
	i=0
	while i < 4**k:
		FrequencyArray.append(0)
		i+=1
	i=0
	while i < len(Text)-k+1:
		Pattern = Text[i:i+k]
		j=PatternToNumber(Pattern)
		FrequencyArray[j]+=1
		i+=1
	return FrequencyArray

data="ACATGTGTTACATCTACGGGTAGTCCAATTATCCCATACGTTGAAAGGACAGTCATGACACGTCTGCTACATCCGCGAGTATGTAAAACCTGGGTAATCTCGAGCGATAACTGAGACTATCATACATAAAGGTTGAGCTGGACAAGTCAAATTTCACGCCGTGCATCGAGGGCATTGTCCGGTTGAGCGGTAATAGATACCTACCACGGCTTGCGTATGAGACCCGCCAAGTTACCGAAGGCCGTACCGTAGGATTCAATGCGTTTATATATGGGAATGTATCTCCCAACCACGGGTTGAAATCGGGCCCAGCACATTGATGGCTCCCCTTTTGGTTCCACCCAGTCCTATATCGCGAGTTTGAATTAAGAGATCGGTCACAATCCCGGGCCGTCGAGTGAATGATTGGTTGGGGTTCGTCAGGAGCAATTGGGAGCAGGGTTCCTGGTCTACCACAATGACCTCGTGCCTAAGAAGTCCTCGTTAGCCCACCCCCCGTGCTAGTTGGGCCCGCTGCTCTCCTGTGCAAATCGACCGTCTGTCCCATGACCATCGCAAGTCTGCTGGGGTACCGCTTACAGGGTCATAAGGTCGGAGATGCGGCTACGCCTAACTGCGCGAGCTATTGTTTACCTGAGAAGTACTCATCCCCTCATCGGTCTGAAACGTAATGACTCATCTCTACCGCTATCTTGAGCAGGTGCGAAATAGTCCCTATTTCCATTCGGATAATGAATCTTGGA"

results=ComputingFrequencies(data,7)

f= open("freqarrayoutput.txt","w")

for i in results:
	print i,

for i in results:
	f.write(str(i)+ " ")
f.close()



def FasterFrequentWords(Text,k):
	FrequentPatterns=[]
	FrequencyArray=ComputingFrequencies(Text,k)
	MaxCount=max(FrequencyArray)
	for i in range(4**k -1):
		if FrequencyArray[i]==MaxCount:
			Pattern=NumbertoPattern(i,k)
			FrequentPatterns.append(Pattern)
	return FrequentPatterns

