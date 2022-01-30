#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'

#Single Loop
"""
for i in range(len(dna)):
	base = dna[i]
	print(i, i % 3, base)

"""
#Nested Loop

for j in range(0, len(dna), 3):
	for k in range(3):
		base = dna[j + k]
		print(j + k, k, base)


"""
python3 24frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
