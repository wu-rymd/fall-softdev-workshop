# Team R (Rachel Ng, Raymond Wu)
# SoftDev1 pd7
# K10 -- Jinja Tuning
# 2018-09-25

from flask import Flask, render_template
from csv import reader
from random import choices

app = Flask(__name__)  # create instance of class Flask

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
        else:
            occupations[ record[0] ] = { "percent" : float( record[1] ),
                                         "link"    : record[2],
                                       }
            
    csvFileObject.close()

#  PRECONDITION: occupations dict cannot be empty (csvToDict must have ran first)
# POSTCONDITION: weights list is populated w/ weighted percentages of randomness
def dictWeights():
    listValues = list(occupations.values()) # list containing values in dictionary
    # the values themselves are dictionaries of the form {'percent': <#.#> , 'link': "..."}

    for dictionary in listValues:             # for each value in occupations dictionary
        weights.append(dictionary['percent']) # put the percentage in list weights

# these accessor methods are necessary b/c
# it doesn't make sense to keep reading the csv file & re-populate the occupations dict
# every time we want to access the data
#
# POSTCONDITION (both functions): occupations{} and weights[] must be populated w/ data
def getOccupationsDict():
    return occupations

def getWeights():
    return weights


# this function is assigned to a route...!
@app.route("/occupations")
def showOccupations():

    return render_template("occupationsTable.html",
                           occupations = getOccupationsDict(),  # `occupation` here refers to Jinja var
                           randomOccupation = choices( list(getOccupationsDict().keys()) , weights = getWeights() )[0]
                           # puts the keys to occupation dict in a list, choose randomly (weighted) from that list
                           # random.choices() returns a k-sized list (default=1) ... only concerned with first output
    )


if __name__ == "__main__":
    # must populate dictionary & list with data
    # these methods are not linked to a Flask route,
    # so not necessary that app is running...
    csvToDict()
    dictWeights()
    
    app.debug = True
    app.run()
