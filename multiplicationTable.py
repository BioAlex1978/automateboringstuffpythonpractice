#! python3
# multiplicationTable.py - takes an integer argument N from the command line and makes a
# spreadsheet with a multiplication table of NxN dimensions, properly filled in
# Automate the Boring Stuff with Python, chapter 13, pg.326, Practice Project

# ALSO: added a feature that, if the argument is not an integer or not given, prompts the user
# to input a non-zero integer to continue or 0 to exit the script

import sys, openpyxl
import pyinputplus as pyip

# First, make sure a command line argument has been passed and that it is an integer
try:
    tableN = int(sys.argv[1])
except:
    print('**ERROR**')
    print('You must pass an integer for this script to operate correctly.')
    print('The correct format is: "multiplicationTable.py N"')
    print('without quotes, where N is a non-zero integer.')
    print()
    print('You may enter an integer now, or enter 0 (zero) to exit the script.')
    tableN = pyip.inputInt(prompt='Enter any integer to continue or 0 to exit: ')
    # It may seem redundant to have this here and repeated below with the error, but
    # it makes more sense to have no error message here, as the user is choosing 0 to exit
    if tableN == 0:
        sys.exit()

if tableN == 0:
    print('ERROR: cannot create a 0x0 multiplication table. Exiting script.')
    sys.exit()

# Create the spreadsheet
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = f'{tableN} x {tableN} Multiplication Table'
# label the rows and columns using the first row and column
for label in range(1, tableN + 1):
    sheet.cell(row = 1, column = label + 1).value = label
    sheet.cell(row = 1, column = label + 1).font = openpyxl.styles.Font(bold = True)
    sheet.cell(row = label + 1, column = 1).value = label
    sheet.cell(row = label + 1, column = 1).font = openpyxl.styles.Font(bold = True)
# Populate it with the multiplication table
for x in range(1, tableN + 1):
    for y in range(1, tableN + 1):
        sheet.cell(row = y + 1, column = x + 1).value = x * y
# save the spreadsheet
wb.save(f'{tableN}x{tableN}MultiplicationTable.xlsx')
print(f'Created the file: {tableN}x{tableN}MultiplicationTable.xlsx')