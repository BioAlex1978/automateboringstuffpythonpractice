#! python3

# text2spreadsheet.py - a program to read the contents of textfiles in the directory and
# write their contents to a spreadsheet in which each column represents a file, and each
# cell in that column contains a line from the text file.
# Automate the Boring Stuff with Python 2e, chapter 13, pg. 328 practice project

# NOTES:
# 1.) The book wants the text contents to start in row one of each column, but
#     I think it's better to make that first cell be the name of the text file
# 2.) For user-friendliness, the spreadsheet sheet gets the title of the directory
# 3.) For clarity, the spreadsheet gets saved as the directory name + "TextFiles.xlsx"

import os, openpyxl, sys

# create a list to hold text file filenames and populate it with the names of textfiles in the current directory
textfiles = []
for file in os.listdir():
    if file.endswith('.txt'):
        textfiles.append(file)

# get the current directory name to use for titles
dirName = os.path.split(os.getcwd())[1]

# first, a bit of sanity checking; there's no reason to run the program if there are no text files
if len(textfiles) == 0:
    print('ALERT: No text (.txt) files found in this directory. Exiting...')
    sys.exit()

# create and set up the spreadsheet
textWb = openpyxl.Workbook()
sheet = textWb.active
sheet.title = dirName + ' Text Files'

# Loop though the file names in textfiles, open the text file, & write its name to the top of a column in the spreadsheet
for i in range(len(textfiles)):
    col = i + 1 # hold the column number, to avoid repetively typing i + 1
    sheet.cell(row = 1, column = col).value = textfiles[i] #+ '\n'
    tfile = open(textfiles[i], 'r')
    tLines = tfile.readlines()
    rowNum = 2 # starting row number for putting in text lines
    # Loop through tLines and put each line of text into a cell in this column
    for line in tLines:
        sheet.cell(row = rowNum, column = col).value = line
        rowNum += 1 # increment the row number
        

# save the spreadsheet and notify the user
ssFileName = ''.join(dirName.split()) + 'TextFiles.xlsx'
textWb.save(ssFileName)
print(f'Text files in this directory inserted into columns of spreadsheet and saved as {ssFileName}.')