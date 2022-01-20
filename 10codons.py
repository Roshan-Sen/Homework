#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

# your code goes here
start = 0
k = 3
for i in range(start, len(dna), k):
	print(dna[i:i + k])

"""
python3 10codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
