#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random
import math

#User input
if len(sys.argv) < 4:
	print('Insufficient input')
	sys.exit()

genomesize = int(sys.argv[1])
readnumber = int(sys.argv[2])
readlength = int(sys.argv[3])

#Build Genome
hitcount = []
for j in range(genomesize): hitcount.append(0)

#Record Hits
for k in range(readnumber):
	start = random.randint(0, genomesize - readlength)
	for l in range(start, start + readlength): hitcount[l] += 1

#Min, Max, Average read count
min = hitcount[readlength - 1]
max = hitcount[readlength - 1]
sum = 0
for value in hitcount[readlength - 1:-readlength]:
	if min > value: min = value
	if max < value: max = value
	sum += value
average = sum / (genomesize - 2 * readlength)
print(min, max, '{:.5f}'.format(average))

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
