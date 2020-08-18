#! python3

# excel2csv.py - reads all of the Excel files in the current directory and converts them
# to CSV files. Each sheet of an Excel file becomes it's own CSV file with the name
# format <excel filename>_<sheet title>.csv
# Automate the Boring Stuff with Python 2e, chapter 16, pg. 388 practice project

import os, openpyxl, csv

# loop through the contents of the current directory
for excelFile in os.listdir('.'):
    if not excelFile.endswith('.xlsx'):
        continue # skip non-excel files by continuing to next iteration
    # load the excel workbook
    print(f'Converting {excelFile} to CSV...')
    wb = openpyxl.load_workbook(excelFile)
    # loop through the sheets in the workbook
    for sheetName in wb.get_sheet_names():
        sheet = wb.get_sheet_by_name(sheetName)
        
        # create the CSV file name from the excel file name and the sheet title
        filename = excelFile[:excelFile.index('.xlsx')] + '_' + sheetName + '.csv'
        csvFile = open(filename, 'w', newline='')
        # creat the csv.writer object for this CSV file
        csvWriter = csv.writer(csvFile)
        
        #loop through every row in the sheet
        for rowNum in range(1, sheet.max_row + 1):
            rowData = [] # append each cell to this list
            # loop through each cell in the row
            for colNum in range(1, sheet.max_column + 1):
                # append each cell's data to rowData
                rowData.append(sheet.cell(row = rowNum, column = colNum).value)
            # write rowData to the CSV
            csvWriter.writerow(rowData)
        # close the finished file
        csvFile.close()