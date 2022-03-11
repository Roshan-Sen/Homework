#!/usr/bin/env python3
# 61dust.py

import argparse
import mcb185 as mcb

# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library

#mask changes means change to lowercase or N's

#setup
parser = argparse.ArgumentParser(description='Masks the low entropy sequences in a sequence file')
# arguments
parser.add_argument('fasta', type=str,
	metavar='<str>', help='required fasta file')
parser.add_argument('--window_size', required=False, type=int, default = 10, 
	metavar='<int>', help='integer window size, default = 10')
parser.add_argument('--entropy_threshold', required=False, type=float, default = 1.0, 
	metavar='<float>', help='floating point entropy threshhold, default = 1.0')
parser.add_argument('--masking_style',required = False, type=str,
	default = 'N-based', metavar='<str>', help='style of masking, either \'N-based\' or \'lowercase\'')
# finalization
arg = parser.parse_args()

#print(arg.fasta, arg.window_size, arg.entropy_threshold, arg.masking_style)

#main program: reads a genome fasta file and returns
#a file with masking

#N-based or not
filestring = ''
if arg.masking_style == 'N-based': nbase = True
else:                              nbase = False

#writing the text for the fasta
for name, record in mcb.read_fasta(arg.fasta):
	filestring = filestring + name + ' \n'
	
	#builds a new record
	newrecord = ''
	for i in range(0, len(record) - arg.window_size + 1, arg.window_size):
		if i + arg.window_size > len(record):
			kmer = record[i:]
		else:
			kmer = record[i:i + arg.window_size]
		newkmer = mcb.masker(kmer, nbase, arg.entropy_threshold)
		newrecord += newkmer
	
	#add the record to the filestring
	#with lines 50 characters long
	linelength = 50
	counter = 0
	for i in range(0, len(newrecord) - linelength, linelength):
		filestring += newrecord[i:i + linelength]
		filestring += '\n'
		counter += linelength
	if len(newrecord) % linelength != 0:
		filestring += newrecord[counter:]
		filestring += '\n'
	else: filestring += '\n'

print(filestring)
