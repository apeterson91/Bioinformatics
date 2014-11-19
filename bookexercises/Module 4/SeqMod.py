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
    
def readindata(filename,option=1):
	f=open(filename,"r")#open file for reading in data
	QuizInput=f.read() # store in memory
	if option==1:
		f.close() # close file and return list
		return QuizInput
	elif option==2:
		QuizDataInput=[]
		Data=QuizInput.split(" ") #separate based upon space formatting
		for datum in Data:
			QuizDataInput.append(int(datum)) #append separately spaced integers into list
		f.close() # close file and return list
		return QuizDataInput
	elif option ==3:
		QuizDataInput=[]
		Data=QuizInput.split("\n") #separate based upon line formatting
		QuizDataInput=[int(datum) for datum in Data]
		f.close()
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
