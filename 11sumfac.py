#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5

# your code goes here

fact = 1
sum = 0
for i in range(1, n + 1):
	fact *= i
	sum += i
print(n, sum, fact)

"""
python3 11sumfac.py
5 15 120
"""
