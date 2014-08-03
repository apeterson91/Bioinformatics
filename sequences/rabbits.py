# How many rabbit pairs will be left after n months if each pair produces a litter of k 
# rabbit pairs

def num_rabbits(n,k):
	baby_bun=1
	bunny_bun=0
	temp = 0
	for i in range(n):
		if i!=0:
			# set the temporary variable to the number of new baby bunnies
			temp= bunny_bun*k
			# convert all the previously baby bunnies into mature bunnies- for next month
			bunny_bun+=baby_bun
			baby_bun=temp
			temp=0
	return baby_bun+bunny_bun
	
nn=int(raw_input("What is the 'n'?"))
kk=int(raw_input("What is the 'k'?"))

print num_rabbits(nn,kk)