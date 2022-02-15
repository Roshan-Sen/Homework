#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

#print(sys.argv)

if len(sys.argv) == 1:
	print('Requires Numerical Input (Separate Numbers with Spaces)')
	sys.exit()

numbers = []
for i in range(1, len(sys.argv)): numbers.append(float(sys.argv[i]))
#print(numbers)
count = len(numbers) #counts number of elements used in calculations

#min, max, and mean calculation/determination
min = numbers[0]
max = numbers[0]
sum = numbers[0]
for j in range(1, count):
	if numbers[j] > max: max = numbers[j] #parses through the set to find min and max
	if numbers[j] < min: min = numbers[j]
	sum += numbers[j]
mean = sum / count #mean calculation

#Std. deviation calculation. Formula used sqrt(E((value - mean)^2)/n)
sumsquares = 0 #variance calculation
for k in range(0, count):
	difference = numbers[k] - mean
	sumsquares += difference ** 2
variance = sumsquares / (count)
stddev = variance ** 0.5 #std deviation calculation

#Median determination
numbers.sort()
if count % 2 == 1: median = numbers[math.floor(count/2)]
else:
	number1 = numbers[count / 2 - 1]
	number2 = numbers[count / 2]
	median = (number1 + number2) / 2

#Printing all values
print('Count:', count)
print('Minimum:', min)
print('Maximum:', max)
print('Mean:', '{:.3f}'.format(mean))
print('Std. dev:', '{:.3f}'.format(stddev))
print('Median:', '{:.3f}'.format(median))

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
