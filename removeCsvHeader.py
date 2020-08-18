#! python3

# removeCsvHeader.py - Removes the header from all CSV files in the current working directory
# and save the modified version into a 'headerRemoved' directory
# Automate the Boring Stuff with Python 2e, chapter 16, pg.378

import os, csv

os.makedirs('headerRemoved', exist_ok = True) # make a directory to hold the modified CSVs

# loop through every file in the current working directory
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip any non-CSV files
    print('Removing header from ' + csvFilename + '...')
    
    # read the CSV file in, while skipping the first row
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue # skip the first row
        csvRows.append(row)
    csvFileObj.close()
    
    # write out the CSV file
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
    print('Modified file saved to ./headerRemoved/' + csvFilename)
# notify the user the job is complete
print('***Header removal complete. Please check ./headerRemoved for the modified CSVs***')