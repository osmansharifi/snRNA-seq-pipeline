import random
from random import choice

#create 2 random 500bp sequences for the fake mecp2_WT and mecp2_MUT chromosomes

def String(length):
	DNA=""
	random.seed(400)
	for count in range(length):
		DNA+=choice("ACGT")
	return DNA
print(String(500))

#Sequences generated via the String function and checked for matches against the
# mouse genome and each other 
mecp2_WT = "TCACCTAAGGGCCCCGGGCTTTATTACTCTCCCCTACGCTAATCGGGTCCTAGTGGGCAATGTCTGCGGCGTACTGA\
TAGAAGTTACAGGTGCGTGGTCCCGAGAGCAATCGCAAAACACGCAGCATTGTAAGGAAGGACAATCGAACAAGCGCGTAGATATAATA\
ACCACGGGCTTGGGCTGCTGGCGTTCGCTACGTTGCTAGGGCCGTTGTGCCACTAGTACTATGACCTTCCCTCGGGTCTGTAGTGTGGA\
GGCGACGACGGGAAGTGACTAAAGAACTGTTTCGATCTTACGGATAGCCTACCCGTCGCCTCCAAGCATAAATATGGGGCGAGGGAAAG\
CGTCCCGCCGCGGTACGAGACACTAGGGAACTTAAGGAAAATGGCAGGGCACTCTCTTAGCTGTATTCAACAGAGTCTATCCGTCCGGC\
GACCTATCGTAACGTGGGTCGCAGAGTAACCATGCATAAATATGCCTGCGGTAACTTCTGACGTTTA"
mecp2_MUT = "ATGTTTCTAGAATATATTTACGAAAAGTATGACGCCCTGTAGTCTCGCTTCTCCGCAACTAAACATACGGGACAGA\
TTGTATGTGGCTAAGTTTACACTGACACCTGCCCCCCCCTCTGGTCGCCCCCGGAGGGAATACGGTCAGCACACCACTGGGCTCATGTG\
AAAGAGCGTTAGCAATTACCCAAATTCGGTGTTACGACTTCAGACTCAAGGAAACAGCTGGCCACGGAAACATGTCGCGATTTAGGCGG\
CCGGTGTTTATCCCGTTCCGGTGTTGTAGATGAGACTGCGCACACACAAAAACCCCTCGACCGGGATTACTCGCTACCCCTCAGTTGTG\
GATGGGTCCCCCAGTGATGCGCCTAGCTTGGAGTCGGGAGCGCGGCCGAGAACGCCTCTTCTTGACTTGTTGAACGGTCACTTAAGACA\
CAACAGTTCGGTACATACTCTGTTTTGGGTGGCCGGTCAATCCTATGACTGGAACCAAATGGCTCAAG"
print("WT_"+mecp2_WT,"MUT_"+mecp2_MUT)