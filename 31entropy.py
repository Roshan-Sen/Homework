#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

#Import user input
import math
import sys
if len(sys.argv) == 1:
	print('Requires Numerical Input (Separate Numbers with Spaces)')
	sys.exit()

#Load probabilities into list
probs = []
sum = 0
tolerance = 0.0001
for i in range(1, len(sys.argv)):
	probs.append(float(sys.argv[i]))
	sum += float(sys.argv[i])

#check if sum is within tolerance
if abs(sum - 1.0) > tolerance:
	print('Probabilities do not sum to 1.0')
	sys.exit()

#Entropy calculation
entropy = 0
for prb in probs:
	entropy += -1 * prb * math.log2(prb)

print('{:.3f}'.format(entropy))

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
