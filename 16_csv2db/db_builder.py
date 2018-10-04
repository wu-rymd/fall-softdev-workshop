# Tina Wong, Raymond Wu (team takingTheW)
# SoftDev1 pd7
# K16 -- No Trouble
# 2018-10-05

import sqlite3              # enable control of an sqlite dabatase
from csv import DictReader  # facilitates CSV I/O

DB_FILE="fakeTalos.db"

db = sqlite3.connect(DB_FILE) # open if file exists, else create
c = db.cursor()               # facilitates CSV I/O

def peeps():
    
    recordList = []
    
    with open('peeps.csv') as csvfile:
        reader = DictReader(csvfile)
        for record in reader:       # for each record in csv
            recordList.append(record)  # append record as dict into recordList

    # create table
    c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER PRIMARY KEY)")

    for record in recordList:
        c.execute("INSERT INTO peeps VALUES ( \"{}\" , \"{}\" , \"{}\" )".format(record['name'] , record['age'] , record['id']) )
        # values must be include string delimiters https://groups.google.com/a/stuy.edu/forum/#!topic/softdev18-19/al0HpOPNE10
        
def courses():
    recordList = []
    with open('courses.csv') as csvfile:
        reader = DictReader(csvfile)
        for record in reader:
            recordList.append(record)

    c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")

    for record in recordList:
        c.execute("INSERT INTO courses VALUES ( \"{}\" , \"{}\" , \"{}\" )".format(record['code'] , record['mark'] , record['id']) )


peeps()
courses()
    
db.commit()
db.close()
