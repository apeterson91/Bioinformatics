## If provided an ExPasy protein ID - query the database
## and find the relevant information

#Example
from Bio import ExPASy
from Bio import SwissProt
handle = ExPASy.get_sprot_raw('H3SRW3') #you can give several IDs separated by commas
record = SwissProt.read(handle) # use SwissProt.parse for multiple proteins
print record.biological_process

# from Bio import ExPASy
# from Bio import SwissProt
# def find_keywords(id):
# 	handle = ExPASy.get_sprot_raw(id)
# 	record = SwissProt.parse(handle)
# 	return record.keywords
# 	
# input=str(raw_input("What is the ID?"))
# 
# print " ".join(find_keywords(input))


