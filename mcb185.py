# mcb185.py

import sys
import gzip
import math

aalist = ['I', 'V', 'L', 'F', 'C', 'M', 'A', 'G', 'T', 'S', 'W', 'Y', 'P', 'H', 'E', 'Q', 'D', 'N', 'K', 'R']
hydropathy = [4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]


#yields fasta file
def read_fasta(filename):
	name = None
	seqs = []

	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()

# def other functions...
def lettercount(seq):
	count = {}
	for aa in seq:
		if aa not in count: count[aa] = 0
		count[aa] += 1
	return count

# kdcount
#calculates mean hydropathy of an amino acid sequence
#does not validate invalid amino acids
def kdcalc(seq):
	sequenceaalist = []
	sum = 0
	for letter in seq: sequenceaalist.append(letter)
	for val in sequenceaalist:
		if aalist.count(val) == 0:
			print('A protein sequence has invalid amino acids')
			sys.exit()
	for aa in seq:
		index = aalist.index(aa)
		sum += hydropathy[index]
	kd = sum / len(seq)
	return kd

#entropy calculator, takes an array of float values
def entropy(probs, tolerance = 0.0001):
	sum = 0
	for prob in probs:
		sum += prob
	if abs(sum - 1.0) > tolerance:
		print('Probabilities do not sum to 1')
		sys.exit()
	entropy = 0
	for prob in probs:
		entropy += -1 * prob * math.log2(prob)
	return entropy

#calculates percent of each nucleotide in a sequence.
#returns value in dictionary
def ntprop(seq):
	ntcount = {'A':0, 'C':0, 'G':0, 'T': 0}
	bases = 'ACGT'
	invalidbase = False
	total = 0
	for nt in seq:
		if nt in bases:
			ntcount[nt] += 1
			total += 1
		else: invalidbase = True
	propA = ntcount['A'] / total
	propC = ntcount['C'] / total
	propG = ntcount['G'] / total
	propT = ntcount['T'] / total
	ntproportion = {'A':propA, 'C':propC, 'G':propG, 'T': propT}
	return ntproportion

#masks a sequence, parameters nbased = True will return
#an N-based mased sequence, else: returns lowercase
#masking. Threshhold is the entropy threshhold 
def masker(seq, nbased, threshhold):
	proportions = ntprop(seq)
	proparray = []
	for nuc in proportions:
		if proportions[nuc] != 0:
			proparray.append(proportions[nuc])
	seqentropy = entropy(proparray)
	if seqentropy > threshhold:
		return seq
	
	if nbased:
		newseq = ''
		for char in seq: newseq += 'N'
	else:
		newseq = seq.lower()
	return newseq
	
#function tester
"""
def functiontester():
	#entropy calculator, should be 1.846
	print('Entropy')
	print(entropy([0.1, 0.2, 0.3, 0.4]))
	#ntproportion
	print('nt proportion')
	print(ntprop('ATCGTGCTAGC'))
	#masker
	print('masker')
	print(masker('ATGTATGTGCA', True, 1.0))
	print(masker('AAAAAAAAAAAAA', False, 1.0))
	print(masker('AAAAAAAAAAAAA', True, 1.0))
"""
"""
functiontester()
"""
