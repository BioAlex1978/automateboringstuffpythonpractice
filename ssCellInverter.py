#! python3

# ssCellInverter.py - a script to invert the coordinates of all cells in a spreadsheet
# It will take the spreadsheet as a command line argument and save the inverted version
# Automate the Boring Stuff with Python 2e, chapter 13, pg.328 Practice Project

# Usage: ssCellInverter.py excelFileName.xlsx

import sys, openpyxl

# First, check that the argument for a spreadsheet file is given and that it can be opened
try:
    origWb = openpyxl.load_workbook(sys.argv[1])
except:
    print('ERROR: Please include a valid spreadsheet to invert.')
    sys.exit()

sheet1 = origWb.active

# create the empty list that will be a list of lists to hold the cell values
sheetData = []

# Fill our sheetData structure with the cell values of the spreadsheet
for col in range(1, sheet1.max_column + 1):
    # create a temporary list in this loop that resets with each iteration
    sheetRow = []
    # populate that list with row values
    for row in range(1, sheet1.max_row + 1):
        sheetRow.append(sheet1.cell(row = row, column = col).value)
    # append that list of row values to sheetData, representing all the values in a column
    sheetData.append(sheetRow)

# create a new spreadsheet
invertedWb = openpyxl.Workbook()
sheet2 = invertedWb.active
sheet2.title = sheet1.title + ' - Inverted'

# Fill the new spreadsheet with data from sheetData, w/ the coordinates inverted
for row in range(len(sheetData)): # here, we use row for what was column above
    for col in range(len(sheetData[row])): # here we use column for what was a row above
        sheet2.cell(row = row + 1, column = col + 1).value = sheetData[row][col] # put the value into that cell

# save the inverted file
filename = sys.argv[1][:sys.argv[1].index('.xlsx')] + '(inverted).xlsx'
invertedWb.save(filename)
print(f'Saved the inverted file as "{filename}".')