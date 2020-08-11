#! python3

# blankRowInserter.py - takes two integers, numRows and atRow, and an Excel file as command line arguments
# and inserts numRows blank lines starting at row atRow into the active spreadsheet
# running the script should look like this: python3 blankRowInserter.py atRow numRows mySpreadsheet.xlsx
# where atRow and numRows are integers greater than zero
# Automate the Boring Stuff with Python 2e, chapter 13, pg.327

import sys, openpyxl

# First check that the arguments are valid, and exit if they aren't
try:
    atRow = int(sys.argv[1])
    numRows = int(sys.argv[2])
    wb = openpyxl.load_workbook(sys.argv[3])
except:
    print('***ERROR***')
    print('Please input valid arguments in the proper format:')
    print('blankRowInserter.py numRows atRow mySpreadsheet.xlsx')
    print('where numRows and atRow are integers greater than zero.')
    sys.exit()

sheetO = wb.active
sheetM = wb.create_sheet(index=0, title=sheetO.title + ' (M)')
# copy the rows up to atRow to sheetM
for row in range(1, atRow):
    for column in range(1, sheetO.max_column + 1):
        sheetM.cell(row=row, column=column).value = sheetO.cell(row=row, column=column).value

# now copy the remaining rows offset by numRows
for row in range(atRow, sheetO.max_row + 1):
    for column in range(1, sheetO.max_column + 1):
        sheetM.cell(row = row + numRows, column = column).value = sheetO.cell(row=row, column=column).value

#finally, delete the original sheet so only the modified sheet remains
del wb[sheetO.title]
# create the filename for the modified file by inserting (modified) before the file suffix
filename = sys.argv[3][:sys.argv[3].index('.xlsx')] + '(modified).xlsx'
# save the modified spreadsheet using the modified filename
wb.save(filename)
print(f'Inserted {numRows} rows at row number {atRow} and saved to "{filename}".')