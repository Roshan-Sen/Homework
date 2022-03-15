import finalprojectgenome as sim

#Prokaryotic Gene Finding
"""
A convenient way to find genes in prokaryotic genomes is to say that any ORF >
100 aa codes for a protein. But how accurate is this practice? Are there a lot
of fake genes in the genome because of this? Using simulations, how many genes
in a genome are probably not real?

+ Simulate a prokaryotic genome
+ Make a histogram of ORF sizes
+ Use various cutoffs and report the number of fake genes found
+ Estimate the number of fake genes in E. coli (for example)
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

#E. coli information
genecount = 4285
#orf sizes will use the defaults set in the genome
#simulator file

"""
----------------------------
Functions for Accuracy Check
----------------------------
"""

#Finds orfs in a single strand genome and returns the
#orfs in a list, checks the other strand as well
def orffinder(genome):
	orflist = []
	#checking first strand
	index = 0
	countingorf = False
	orflistindex = -1
	while index < len(genome) - 2:
		codon = genome[index:index + 3]
		if countingorf:
			if gcode[codon] == '*':
				countingorf = False
				orflist[orflistindex] += codon
				index += 1
			else:
				orflist[orflistindex] += codon
				index += 3
		elif codon == 'ATG':
			countingorf = True
			orflistindex += 1
			orflist.append('ATG')
			index += 3
		else: index += 1
	lastorf = orflist[len(orflist) - 1]
	if lastorf[len(lastorf) - 3:] not in list(sim.stopcodons.keys()):
		orflist.pop()
	#checking the reverse strand
	otherstr = sim.reversecomplement(genome)
	rindex = 0
	countingorf = False
	while rindex < len(otherstr) - 2:
		codon = otherstr[index:index + 3]
		if countingorf:
			if gcode[codon] == '*':
				countingorf = False
				orflist[orflistindex] += codon
				rindex += 1
			else:
				orflist[orflistindex] += codon
				rindex += 3
		elif codon == 'ATG':
			countingorf = True
			orflistindex += 1
			orflist.append('ATG')
			rindex += 3
		else: rindex += 1
	newlastorf = orflist[len(orflist) - 1]
	if newlastorf[len(newlastorf) - 3:] not in list(sim.stopcodons.keys()):
		orflist.pop()
	return orflist

#extracts the orf length in amino acids from a list of ORFs
#stores lengths in an array
def orflengths(orfarray):
	orflen = []
	for orf in orfarray:
		length = len(orf) / 3 - 1
		orflen.append(length)
	return orflen

#Finds common orfs between a 'real' set of orfs
#and a computed set function
def commonorfs(realset, foundset):
	commonelements = []
	for i in range(len(realset)):
		realentry = realset[i]
		for j in range(len(foundset)):
			if realentry == foundset[j]:
				commonelements.append(realentry)
				break
	return commonelements

#Function Tester
"""
def functiontester():
	samplegenelibrary = sim.genomelibrary(100)
	sampleorfs = sim.extractorfs(samplegenelibrary)
	samplegenome = sim.buildgenome(samplegenelibrary)
	samplefoundorfs = orffinder(samplegenome)
	samplecommonorfs = commonorfs(sampleorfs, samplefoundorfs)
	print(samplecommonorfs)
	

functiontester()
"""

#main program: build a bacterial genome, run an orf finder
#function and see whether the orfs line up to the ones built
#into the genome
ecgenelib = sim.genomelibrary(genecount)
ecorfs = sim.extractorfs(ecgenelib)
ecgenome = sim.buildgenome(ecgenelib)
ecfoundorfs = orffinder(ecgenome)
eccommonorfs = commonorfs(ecorfs, ecfoundorfs)

print('The simulated genome contained ' + str(len(ecgenelib)) + ' orfs.')
print('The number of orfs found in the genome was ' + str(len(ecfoundorfs)) + '.')
print('The number of found orfs that were \"real\" was ' + str(len(eccommonorfs)) + '.')


