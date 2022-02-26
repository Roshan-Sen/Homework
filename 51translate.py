#!/usr/bin/env python3
# 51translate.py

import sys

# Make a program that translates coding sequences into proteins
# You have been provided with the genetic code as a dictionary
# Use the actin sequence in the Data directory

gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}

if len(sys.argv) != 2:
	print('Insufficient or too much input')
	sys.exit()

#checks if there is an invalid base in a DNA sequence
def invalidbase(kmer):
	bases = 'ACGT'
	for nt in kmer:
		if nt not in bases:
			return True
	return False

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

#Translates a coding strand of DNA, returns if there is an
#invalid base as well, adds X if invalid base
def translatedna(sequence, frame = 0):
	protsequence = ''
	invalidnt = False
	for i in range(frame, len(sequence) - 2, 3):
		segment = sequence[i:i + 3]
		if invalidbase(segment):
			protsequence += 'X'
			invalidnt = True
		else: protsequence += gcode[segment]
	return protsequence, invalidnt

#main program
name, seq = fastareader(sys.argv[1])
protseq, baseerror = translatedna(seq[0].upper())
print(protseq)
if baseerror:
	print('Invalid Base In Sequence (amino acid replaced with X)')

"""
python3 51translate.py ../Data/act1.fa
MCDDEVAALVVDNGSGMCKAGFAGDDAPRAVFPSIVGRPRHQGVMVGMGQKDSYVGDEAQ
SKRGILTLKYPIEHGIVTNWDDMEKIWHHTFYNELRVAPEEHPVLLTEAPLNPKANREKM
TQIMFETFNTPAMYVAIQAVLSLYASGRTTGVVLDSGDGVTHTVPIYEGYALPHAILRLD
LAGRDLTDYLMKILTERGYSFTTTAEREIVRDIKEKLCYVALDFEQEMATAASSSSLEKX
YELPDGQVITVGNERFRCPEAMFQPSFLGMESAGIHETSYNSIMKCDIDIRKDLYANTVL
SGGTTMYPGIADRMQKEITALAPSTMKIKIIAPPERKYSVWIGGSILASLSTFQQMWISK
QEYDESGPSIVHRKCF*
"""
