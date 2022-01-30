#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
reverseComplement = ''
for i in range(len(dna) - 1, -1, -1):
	#print(i)
	base = dna[i:i + 1]
	if base == 'A': reverseComplement += 'T'
	elif base == 'T': reverseComplement += 'A'
	elif base == 'C': reverseComplement += 'G'
	else: reverseComplement += 'C'
print(reverseComplement)

"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
