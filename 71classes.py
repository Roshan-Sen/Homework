import sys
import mcb185 as mcb
import argparse
"""
Using classes to build a library of found 
orfs from an fa file. Using
chromosome 1 of A. thaliana.
I wanted to see how many found 
open reading frames were longer
than a certain threshold.
Object use is unnecessary,
but I wanted to try using them.
"""
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

stopcodons = [
	'TAA', 'TAG', 'TGA'
]

parser = argparse.ArgumentParser(description = 'Finds possible open reading frames in a genome or chromosome sequence and tells user how many have a length in amino acids greater than their specified threshold')
# arguments
parser.add_argument('fasta', type=str,
	metavar='<str>', help='required fasta file')
parser.add_argument('--threshold', required=False, type=int, default = 40, 
	metavar='<int>', help='integer threshold, default = 40')
# finalization
arg = parser.parse_args()

class Gene:
	genesequence = ""
	def __init__(self, genesequence):
		self.genesequence = genesequence
	
	def translation(self):
		aasequence = ""
		for i in range(0, len(self.genesequence), 3):
			codon = self.genesequence[i:i + 3]
			if codon not in list(gcode.keys()): aasequence += "X"
			else:  aasequence += gcode[codon]
		return aasequence
	
def buildgenearray(dna):
	initialgenes = []
	currentgeneindex = -1
	for i in range(3):
		countingorf = False
		for j in range(i, len(dna) - 2, 3):
			codon = dna[j:j + 3]
			if countingorf:
				initialgenes[currentgeneindex] += codon
				if codon in stopcodons:
					countingorf = False
			elif codon == "ATG":
				countingorf = True
				initialgenes.append(codon)
				currentgeneindex += 1
			else: continue
	validgenes = []
	for gene in initialgenes:
		if gene[-3:] in stopcodons:
			validgenes.append(gene)
	return validgenes

def buildgeneobjectarray(genes):
	geneobjarray = []
	for gene in genes:
		geneobject = Gene(gene)
		geneobjarray.append(geneobject)
	return geneobjarray

if len(sys.argv) != 2:
	print("Insufficient or too much input")
	sys.exit()

sequences = []
for record in mcb.read_fasta(arg.fasta):
	sequences.append(record)

chromosome = sequences[0][1]
genes = buildgenearray(chromosome)
geneobjectarray = buildgeneobjectarray(genes)

count = 0
for gene in geneobjectarray:
	if len(gene.translation()) > arg.threshold: count += 1

print("Out of the " + str(len(genes)) + " found orfs, " + str(count) + " orfs had a length greater than the threshold of " + str(arg.threshold) + " amino acids.")
