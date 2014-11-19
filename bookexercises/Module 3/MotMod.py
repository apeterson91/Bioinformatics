#reads in data file of integers storing them in one list
def readindata(filename):
    f=open(filename,"r")#open file for reading in data
    QuizInput=f.read() # store in memory
    QuizDataInput=[]
    Data=QuizInput.split(" ") #separate based upon space formatting
    for datum in Data:
        QuizDataInput.append(int(datum)) #append separately spaced integers into list
    f.close() # close file and return list
    return QuizDataInput

#reads in data file of text, storing them in one list
def readintextdata(filename,option=False):
	f=open(filename,"r")
	Input=f.read()
	Text=[]
	if option==False: 
		Data=Input.split(" ")
	else:
		Data=Input.split("\n")
	for datum in Data:
		Text.append(str(datum))
	f.close()
	return Text
	
def NumberToPattern(index,k):
	if k==1:
		return NumberToSymbol(index)
	quotient = index/4
	remainder = index % 4
	PrefixPattern = NumberToPattern(quotient,k-1)
	symbol= NumberToSymbol(remainder)
	return PrefixPattern + symbol

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

def readinmatrix(filename):
    f=open(filename,"r")
    Data=f.read()
    Data=Data.split("\n")
    stg=[];mat=[]
    for datum in Data:
        moredata=datum.split(" ")
        for number in moredata:
            stg.append(float(number))
        mat.append(stg)
        stg=[]
    return mat