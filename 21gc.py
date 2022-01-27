#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods
import math
dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

gccount = 0;
for i in range(len(dna)):
	base = dna[i:i + 1]
	if base == 'C' or base == 'G':
		gccount += 1

gcpercent = gccount / len(dna)
#print(gcpercent)
print('%.2f' % gcpercent)
print('{:.2f}'.format(gcpercent))
print(f'{gcpercent:.2f}')

"""
python3 21gc.py
0.42
0.42
0.42
"""
