import korflib
import sys

#Make sure command line has 2 arguments
assert(len(sys.argv) == 2)

#Make the length of each sequence line 60 bases long
def wrap(seq, step=60):
	for i in range(0, len(seq), step):
		print(seq[i:i+step])
		
#Read in fasta file and change specific sequences into Ns
for id, seq in korflib.read_fasta(sys.argv[1]):
	if id.startswith("X"):
		beg = 74026592
		end = 74085597
		mut = 74085586
		mx = seq[:beg] + "N"*(end-beg) + seq[end:]
		print(f">{id}")
		wrap(mx)
		print(">Mecp2_e1")
		wrap(seq[beg:end])
		print(">Mecp2_e2")
		wrap(seq[beg:mut] + "t" + seq[mut+1:end])
	else:
		print(f">{id}")
		wrap(seq)
	