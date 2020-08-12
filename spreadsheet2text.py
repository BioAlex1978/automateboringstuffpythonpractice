#! python3

# spreadsheet2text.py - a program to take the contents of a spreadsheet and output it as
# text files, where each text file is generated from a column of the spreadsheet, and each
# line in the text file is generated from a cell in that column
# Automate the Boring Stuff with Python 2e, chapter 13, pg. 328 practice project

# Usage: spreadsheet2text.py mySpreadsheet.xlsx

# NOTES:
# 1.) This program takes the spreadsheet as a command line argument
# 2.) Text files are saved in a new directory named for the spreadsheet (minus .xlsx), in the
#     current working directory
# 3.) Text files will have as many lines as the longest column in the spreadsheet,
#     so some may end with many linebreaks. Not sure how best to get around that.

import sys, os, openpyxl

# First, make sure a valid spreadsheet has been passed as a command line argument
try:
    ssFileName = sys.argv[1]
    wb = openpyxl.load_workbook(ssFileName)
    sheet = wb.active
except:
    print('***ERROR***')
    print('This program needs a valid .xlsx spreadsheet as a command line argument.')
    print('Usage: spreadsheet2text.py mySpreadsheet.xlsx')
    print('Please try again.')
    sys.exit()

# make the directory to hold the text files, using the name of the spreadsheet file w/out '.xlsx'
newDirName = './' + ssFileName[:ssFileName.index('.xlsx')]
try:
    os.mkdir(newDirName)
except:
    print(f'Directory "{newDirName}" already exists. Continuing...')
# change to that directory to produce the text files
os.chdir(newDirName)

print('Converting spreadsheet to text files...')
# Loop through the columns to make the text files for each one. 
for colNum in range(1, sheet.max_column + 1):
    textFile = open(('Column' + openpyxl.utils.get_column_letter(colNum) + '.txt'), 'w')
    # Loop through the rows of this column and write each cell as a line in the textFile
    for rowNum in range(1, sheet.max_row + 1):
        line = sheet.cell(row=rowNum, column=colNum).value
        if line: # check that there was anything in the cell
            if line.endswith('\n'): # checks that the content of the cell ends with a newline
                textFile.write(line)
            else: # add a new line to any content that doesn't end with one
                textFile.write(line + '\n')
        else: # if the cell was empty, line is NoneType an so, false, so just write a newline in the text file
            textFile.write('\n')
    print(f'Created text file named "{textFile.name}".')
    textFile.close()

print('Converstion complete.')
