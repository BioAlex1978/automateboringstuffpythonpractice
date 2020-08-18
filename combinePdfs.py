#! python3

# combinePdfs.py - Combines all the PDFs in the current working directory into a single PDF.
# Automate the Boring Stuff with Python 2e, chapter 15, pg.358
# NOTE: as most PDFs have a cover page for their first page, this script will skip the first page
# and start combining from the second

import PyPDF2 as pydf # For my own convenience, pydf is easier to type
import os # To get directory contents

# Get all the PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

# sort the pdfFiles into alphabetical order
pdfFiles.sort(key = str.lower)

# create the PDF writer object to make the combined PDF
pdfWriter = pydf.PdfFileWriter()

# Loop through the PDF files
for filename in pdfFiles:
    pdfReader = pydf.PdfFileReader(open(filename, 'rb')) # the book has this separated as two commands
    # Loop through all the pages except the first and add them to the writer
    for pageNum in range(1, pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum)) # again, the book has this separated as two commands

# Save the resulting PDF to a file named for the current working directory + '-pdfs-combined.pdf'
pdfOutput = open(os.path.basename(os.getcwd()) + '-pdfs-combined.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()