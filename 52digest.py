#!/usr/bin/env python3
# 52digest.py

import re
import sys
import math

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments
sample = 'actagatcgatgactagctccgtcgattctcgatcgatcaagctcgat'
samplesite = 'ctag'
bases = 'acgt'

if len(sys.argv) != 3:
	print('Insufficient or too much input')
	sys.exit()

#locates restriction cutting sites, returns in an array
def findsites(sequence, site):
	splices = []
	for match in re.finditer(site, sequence):
		splice = match.start()
		splices.append(int(splice))
	return splices

#creates array of digest fragments from a sequence
#and array of splice sites
def splicer(sequence, indeces):
	segments = []
	previoussite = 0
	for i in range(len(indeces)):
		segments.append(sequence[previoussite:indeces[i]])
		if i == len(indeces) - 1:
			segments.append(sequence[indeces[i]:])
		previoussite = indeces[i]
	return segments

#reads a .gb file and returns the DNA sequence in a string
def readgbdna(filename):
	dnaseq = ''
	with open(filename) as fp:
		startingflag = False
		endingflag = False
		for line in fp.readlines():
			linetext = line.rstrip()
			if len(linetext) >= 6 and linetext[0:6] == 'ORIGIN':
				startingflag = True
				continue
			if startingflag:
				for char in linetext:
					if char in bases:
						dnaseq += char
	return dnaseq

#Sample
"""
sites = findsites(sample, samplesite)
spliceddna = splicer(sample, sites)
print(spliceddna)
"""

#main program

dna = readgbdna(sys.argv[1])
sites = findsites(dna, sys.argv[2])
spliceddna = splicer(dna, sites)
for segment in spliceddna:
	print(len(segment))

"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""
