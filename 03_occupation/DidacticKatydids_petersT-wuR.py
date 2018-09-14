# Didactic Katydids -- Theodore Peters, Raymond Wu
# SoftDev1 pd7
# K06 -- Stl/O: Divine your Destiny!
# 2018-09-14

from os import getcwd
# 'getcwd' method from 'os' module -- Return a string representing the current working directory. <0>

from os.path import isfile
# 'isfile' method from 'os.path' module -- Return True if [specified] path is an existing regular file. <1>

from random import random
# imports the 'random' method from the 'random' module <2>                                                                                                                                                                                                               
# Return the next random floating point number in the range [0.0, 1.0)
# Return a k sized list of elements chosen from the population with replacement.                                                                                                                                                                                           
# If a weights sequence is specified, selections are made according to the relative weights.  

from csv import reader
# imports the 'reader' method from the 'csv' module to parse through csv file <3>


# Repeatedly prompts user for a file from working directory until they select a valid file.
#   prompt specifies prompt text.
def getPath(prompt, defaultPath):
    while True:
        userin = input(prompt)
        path = getcwd() + "/" + userin
        if userin == "":
            return path + defaultPath
        if isfile(path):
            return path
        print("File not found. Try again.\n")

# Reads occupations.csv, returns a dictionary with occupation-string keys and weighted-floating-point values
def csvToDict():
    # prepare an occupations dictionary to be returned...
    occupations = {}

    # open the csv file object, bind to variable
    csvFileObject = open(getPath("Choose file name. Leave blank for occupations.csv. | ", "occupations.csv"), 'r')
    # read the records in the csv
    readerObject = reader(csvFileObject)
    
    for record in readerObject:
        # skip over the first & last records
        if record[0] == "Job Class" or record[0] == "Total":
            continue
        # record[0] is the occupation string, record[1] is the floating point (as a string)
        # must convert appropriate string into floating point before placing as value in dict
        else:
            occupations[ record[0] ] = float(record[1])
            
    csvFileObject.close()
    return occupations

# Picks a random dict value based on the weigts given in a dict of strings to their weights.
def weightedRandom(wc, total = None):
    if total == None: # If the total of the weights is known, can avoid calculating sum
        total = sum(wc.values()) # Possibly useful if finding weighted random several times.
    endWeight= total * random() # endWeight in correct range when curWeight >= endWeight
    curWeight = 0
    for i in wc:
        curWeight += wc[i]
        if curWeight >= endWeight:
            return i # dict value.
    raise ValueError("Value of total passed was incorrect.") # If the function gets here,
                                                             # user passed a total value that
                                                             # was wrong.


dict = csvToDict()
print( weightedRandom(dict) )

    
# References
# <0> https://docs.python.org/3/library/os.html#os.getcwd
# <1> https://docs.python.org/3/library/os.path.html#os.path.isfile
# <2> https://docs.python.org/3/library/random.html#random.choices
# <3> https://docs.python.org/3/library/csv.html#csv.reader
