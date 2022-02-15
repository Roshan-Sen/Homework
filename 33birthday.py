#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

trialcount = 1000
population = 25
calendarlength = 365

#Shared Birthday loop
incidence = 0
for j in range(trialcount):
	sharecount = 0
	calendar = []
	for i in range(calendarlength): calendar.append(0)
	for k in range(population):
		position = random.randint(0, calendarlength - 1)
		calendar[position] = calendar[position] + 1
	for hitcount in calendar: 
		if hitcount > 1: 
			sharecount += 1
			break
	if sharecount > 0: incidence += 1

#Display probability
prb = incidence / trialcount
print('{:.3f}'.format(prb))

"""
python3 33birthday.py
0.571
"""

