import sys
import subprocess
import os.path
import html2text
import json
import re
#Second revison: Alpha 1.2
#Issues Adressed: line break have been removed after each cell in data table,
#output looks clean and well tranferrable to data tables
#install pdftohtml, pip install pdftohtml
#Please input full file path to pdf on local system
#Iterate through all arguments to script, and run conversion program on each
#Usage :
#PdfToHTML <pdffilename> <number of columns in PDF Table>
#For now this number is used to tabulate data, this is the Alpha 1.2 version of the
#script still much to do. Testing has been limited, but so far so good
#Issues:
#and knowledge of the number of columns in each PDF table is required,
#Script is scalable and can be automated however(we can work around this)


subprocess.call(["pdftohtml", "-noframes", sys.argv[1]])


#Now find a way to scrape the HTML data from these files, and place them in tabular
##format
#first we collect all data in list, and remove unwanted entries
def ProcessList():
    temp = os.path.splitext(sys.argv[1])[0]
    htmfile = temp + ".html"
    f = open(htmfile, 'r')
    data = []
    for line in f:
        data.append(html2text.html2text(line))
        newdata = []
        for x in data:
            if '*' in x  or x == '\n' or x == '\n\n':
                continue
            else:
                newdata.append(x)

    return newdata

#Tabulate data and convert to JSON Array
# Here we require some method of grabbing columns, if not supplied as input
def Tabulate(newdata,columns):
    columns = int(columns)
    size = len(newdata)
    Columns = []
    Rows = []
    n=0
    #patch to fix line break issue
    pattern = "[a-zA-Z0-9]+"
    temp = []
    for x in newdata:
        match  = re.search(pattern,x)
        temp.append(match.group())
    newdata = temp
    
    rows = (len(newdata)//columns - columns)
    while n < (columns - 1):
        Rows.append(Columns)
        Columns.append(newdata[n + 1])
        Columns = []
        n=n+1

    for j in range(columns - 1):
        for i in range(0,rows):
            Rows[j].append(newdata[(columns + j) + (columns*i)])

    return json.dumps(Rows)



print(Tabulate(ProcessList(),sys.argv[2]))

    
