# Theodore Peters, Raymond Wu (iDoKnow)
# SoftDev1 pd7
# K6 -- StI/O: Divine your Destiny!
# 2018-09-14

from random import choices
# imports the 'choices' method from the 'random' module 
# https://docs.python.org/3/library/random.html#random.choices

# random.choices(population, weights=None ...)
# Return a k sized list of elements chosen from the population with replacement.
# If a weights sequence is specified, selections are made according to the relative weights.

# TODO import csv module

occupations = {}

# TODO parse thru csv, populate occupations dict

def getOccupation():
    # list of occupation strings -- copied into popluation parameter of random.choices()
    # list of weight floating points -- copied into the weights parameter of random.choices()
    return random.choices(occupations.keys(), weights=occupations.values())

# getOccupation()
