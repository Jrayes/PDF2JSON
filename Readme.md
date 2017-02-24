=================================================PDF2JSON======================================================
*==============================================================================================================*

PDF2JSON: A lightweight and simple application that converts PDF files to JSON strings, ready for database insertion. 
  USAGE: PDFtoJSON.py <pdffilename> <number of columns in PDF Table>
  This application is recommended for use in conjuction with a batch PDF processing script, that iterates
  through PDF files in a directory, and applies the scripts usage on each of them. 
  However PDF files can be aggregated and then applied to this script for similar results.
CHANGES MADE: 
Linebreaks removed from before and after data in each cell of PDF table.
CURRENT VERSION:
 1.2 Alpha

DEPENDENCIES: 
pdftohtml
(pip install pdftohtml)

*==============================================================================================================*
