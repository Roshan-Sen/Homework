#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix

aalist = ['I', 'V', 'L', 'F', 'C', 'M', 'A', 'G', 'T', 'S', 'W', 'Y', 'P', 'H', 'E', 'Q', 'D', 'N', 'K', 'R']
hydropathy = [4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]

if len(sys.argv) != 2:
	print('Insufficient or too much input')
	sys.exit()

#calculates mean hydropathy of an amino acid sequence
#does not validate invalid amino acids
def kdcalc(seq):
	sequenceaalist = []
	sum = 0
	for letter in seq: sequenceaalist.append(letter)
	for val in sequenceaalist:
		if aalist.count(val) == 0:
			print('A protein sequence has invalid amino acids')
			sys.exit()
	for aa in seq:
		index = aalist.index(aa)
		sum += hydropathy[index]
	kd = sum / len(seq)
	return kd

#returns true if a sequence has no proline
def noproline(seq):
	for aa in seq:
		if aa == 'P': return False
	return True

#returns true if a full protein sequence contains a 
#hydrophobic helix, given a sequence that had a signal sequence
def helixpresent(seq, length, threshold):
	for i in range(len(seq) - length + 1):
		roi = seq[i:i + length]
		kdvalue = kdcalc(roi)
		if kdvalue > threshold and noproline(roi): return True
	return False

#fasta reader
def fastareader(filename):
	sequenceid = []
	sequences = []
	currentindex = -1
	with open(filename) as fp:
		for line in fp.readlines():
			if line[0] == '>':
				words = line.split()
				sequenceid.append(words[0][1:])
				sequences.append('')
				currentindex += 1
			elif line[0] == ' ' or line[0] == '\n':
				continue
			else:
				linetext = line.rstrip()
				if linetext[len(linetext) - 1] == '*':
					sequences[currentindex] += linetext[0:len(linetext) - 1]
				else:
					sequences[currentindex] += linetext
	return sequenceid, sequences

#main program, finding proteins with signal sequence
#and a transmembrane domain
id, seqlist = fastareader(sys.argv[1])
for j in range(len(id)):
	if len(seqlist[j]) < 30: continue
	if helixpresent(seqlist[j][0:30], 8, 2.5) and helixpresent(seqlist[j][30:], 11, 2.0): print(id[j])

"""
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
