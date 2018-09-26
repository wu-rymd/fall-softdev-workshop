# Team R (Rachel Ng, Raymond Wu)
# SoftDev1 pd7
# K10 -- Jinja Tuning
# 2018-09-25

from csv import reader
from random import choices


occupations = {}
weights = []

# POSTCONDITION: occupations dict is populated with occupation data
def csvToDict():
    csvFileObject = open('./data/occupations.csv', 'r')  # open the csv file object in 'read' mode
    readerObject = reader(csvFileObject)  # read the records in the csv

    for record in readerObject:
        if record[0] == "Job Class" or record[0] == "Total":  
            continue  # skip the first and last records
        
        # record[0] is occupation string, record[1] is floating point (as a string), record[2] is link
        # must convert the appropriate string into floating point before placing as value in dict
        # occupation : [ <percentage> , <link> ]
        else:
            occupations[ record[0] ] = [ float( record[1] ) , record[2] ]
            
    csvFileObject.close()

#  PRECONDITION: occupations dict cannot be empty (csvToDict must have ran first)
# POSTCONDITION: weights list is populated w/ weighted percentages of randomness
def dictWeights():
    listValues = list(occupations.values()) # list containing a list of the values in occupations dict
    # the values themselves are lists of the form [ <percentage> , <link> ]

    for listOfOccupationData in listValues:             # for each value in current list of occupation data
        weights.append( listOfOccupationData[0] )       # put the percentage in list of weights

# these accessor methods are necessary b/c
# it doesn't make sense to keep reading the csv file & re-populate the occupations dict
# every time we want to access the data
#
# POSTCONDITION (both functions): occupations{} and weights[] must be populated w/ data
def getOccupationsDict():
    return occupations

def getWeights():
    return weights
