#!/usr/bin/env python3

import random
#random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence


dna = ''
length = 30
chance = 0.6
#length = 300

for i in range(length):
	num = random.random()
	num2 = random.random()
	if num < chance:
		if num2 < 0.5: dna += 'A'
		else:          dna += 'T'
	else:
		if num2 < 0.5: dna += 'C'
		else:          dna += 'G'

#print(dna)
atcount = 0;
for i in range(len(dna)):
	if dna[i] == 'A' or dna[i] == 'T': atcount += 1

atfraction = atcount / len(dna)
print(len(dna), atfraction, dna)
#print(len(dna), atfraction)
"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
