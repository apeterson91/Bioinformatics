from Bio.Seq import Seq

my_seq = Seq("CAATCTGTACGTTGAGCAAAACTCGACCAATTCTACCCCCTCATTAACAGACCGACATTGTAGTTCTATAGTTGTGGCTCACACCTACTGAAGTATTTGAGTACTTCCGGAATCTTTGGGAGGGAAAGGCCGACTGTGCCATAGTCAGACAACGTCAGAGAATATGCCTTTAGCACATTATAACTTATTCAGTCATAGAACCCGCCCGCGGATACAGATGATATGGCAGGAACTTTTACTAGGTCTAGTAGGGTCCACCGCATTGAGCTGAATATATCGTGCATGGCTCTATCTACGTCTATGCCCTCCACGGTCCTTTGGCAAACGGCGCGCCTTAGAAGTATGGGTTATTTATTCCCGAGAGTAACCTTAGCGAGACACCAGGGTACTTGCAAGAGTATGAGCCGGGCTCCAGACGTTCACTTGACGGGAATTCTGTCTAGGTCGTGAGCATTTTGTCTCAATGGCTCTCCAGCAATCTCGAACGTACCAGAGACTTAGAGGGGATTCACACGAAAAATACGTTTTCGGCGAATTCACAGCAACCGGAAAAAAGAAGGAAATGCGGTGCGAAAGTCACAGACCCACGACTAGACGAGGACACGTTGTTGACGCAACAATTCGCGTAGGGATAGTCAAACGCGACGAACCAGAGAGGATATATGTCCCCCCACGTTGGTGCACCTTTGAACGACACCCTTGACTTCTCGTGGTACTGACCTCTTACGGTCCCTCAAACACTGTGTATTGAACGAATTGTTCGTGACTGATGTGTAGCAAGTCCGTGCAGGGATTGCCTATCCAATATGCCTACATCTTTAAAGATGGGCCCCGAGAAA")

nucleotides = ["A", "C","G","T"]
for i in range(4):
	print my_seq.count(nucleotides[i])