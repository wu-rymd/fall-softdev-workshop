# Team R (Rachel Ng, Raymond Wu)
# SoftDev1 pd7
# K10 -- Jinja Tuning
# 2018-09-24

from flask import Flask, render_template
from csv import reader
from random import choice

app = Flask(__name__)  # create instance of class Flask

# this function is not assigned to a route!
# returns a dictionary with occupation data
def csvToDict():
    occupations = {}  # prepare dict for occupation data 
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
    return occupations

# this function is assigned to a route...
@app.route("/occupations")
def showOccupations():
    return render_template("occupationsTable.html",
                           occupations = csvToDict(),  # `occupation` here refers to Jinja var
                           randomOccupation = choice( list(csvToDict().keys()) ),
                           # puts the keys to occupation dict in a list, choose randomly from that list
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
