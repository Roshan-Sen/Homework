#!/usr/bin/env python3
# 50kmers.py

import sys

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k
sample = 'ATCGTAGCTAGCTGGATCGATCGAT'

if len(sys.argv) != 3:
	print('Insufficient or too much input')
	sys.exit()

#Builds kmer library and counts total
def kmerdictionary(sequence, k):
	total = 0
	kmerdict = {}
	for i in range(len(sequence) - k + 1):
		kmer = sequence[i:i + k]
		if kmer not in kmerdict: kmerdict[kmer] = 0
		kmerdict[kmer] += 1
		total += 1
	return kmerdict, total

#fasta reader (reused from 40 example)
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

#main program
name, seq = fastareader(sys.argv[1])
count, total = kmerdictionary(seq[0], int(sys.argv[2]))

for kmer in sorted(count):
	print(kmer, count[kmer], '{:.4f}'.format(count[kmer] / total))

"""
python3 50kmers.py ../Data/chr1.fa 2
AA	33657	0.1106
AC	15836	0.0520
AG	18244	0.0600
AT	27223	0.0895
CA	18965	0.0623
CC	10517	0.0346
CG	8147	0.0268
CT	18142	0.0596
GA	19994	0.0657
GC	9673	0.0318
GG	10948	0.0360
GT	16348	0.0537
TA	22344	0.0734
TC	19744	0.0649
TG	19624	0.0645
TT	34869	0.1146
"""
