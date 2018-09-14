# Theodore Peters, Raymond Wu (DidacticKatydids)
# SoftDev1 pd7
# K6 -- StI/O: Divine your Destiny!
# 2018-09-14


from random import choices
# imports the 'choices' method from the 'random' module <1>

# random.choices(population, weights=None ...)
# Return a k sized list of elements chosen from the population with replacement.
# If a weights sequence is specified, selections are made according to the relative weights.

from csv import reader
# imports the 'reader' method from the 'csv' module to parse through csv file <4>


# Reads occupations.csv, returns a dictionary with occupation-string keys and weighted-floating-point values
def csvToDict():
    # prepare an occupations dictionary to be returned...
    occupations = {}

    # open the csv file object, bind to variable
    csvFileObject = open('occupations.csv', 'r')
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

# Uses random.choice() to randomly return an occupation according to its weight
def getOccupation():
    # <dictionary>.keys() returns a dict_keys object <5>
    # we need to convert this into a list to be compatable with random.choices()

    # random.choices() returns a k-sized list (default=1) ... only concerned with 1 output
    return choices( list(csvToDict().keys()) , weights=csvToDict().values() )[0]

print( getOccupation() )


# References
# <1> https://docs.python.org/3/library/random.html#random.choices
# <2> https://docs.python.org/3/library/os.html#os.getcwd
# <3> https://docs.python.org/3/library/os.path.html#os.path.isfile
# <4> https://docs.python.org/3/library/csv.html#csv.reader
# <5> https://docs.python.org/3/library/stdtypes.html#dict.keys
