#! python3
# resizeAndAddLogo.py - Resizes all images in the current working directory to fit
# in a SQUARE_FIT_SIZE square, and adds LOGO_FILENAME (which must be in the same 
# directory) to the lower-right corner.
# Automate the Boring Stuff with Python 2e, ch.19, pg.461

# NOTE: end of chapter practice project #1 (pg.470): add the ability to also process GIF and BMP
# as well as make the file extension case-insensitive

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogosm.png'
filetypes = ['.jpg', '.png', '.gif', '.bmp']

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok = True) # create the directory to receive the modified images

# loop over all the files of the current working directory
for filename in os.listdir('.'):
    try:
        suffix = filename[filename.rindex('.'):].lower() # get the filetype suffix to check against filetypes; lower() makes it case insensitive
    except: # in the case that the filename does not contain a period, ignore it
        continue
    if filename == LOGO_FILENAME:
        continue # skip the logo file itself
    elif suffix not in filetypes: 
        continue # skip non-image files
    # load the image for this iteration and get its width and height
    im = Image.open(filename)
    width, height = im.size
    
    # check that the image is large enough to add a logo to ( > 2x the height and width of the logo)
    if not ((width >= 2 * logoWidth) and (height >= 2 * logoHeight)):
        print(f'{filename} is too small to add logo. Skipping...') # notify the user
        continue # skip images that are too small
    
    # check if the image needs to be resized
    # NOTE: the book says 'and' in this statement, but I think it should be 'or'
    if width > SQUARE_FIT_SIZE or height > SQUARE_FIT_SIZE:
        # calculate the new width and height to resize to
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        # resize the image using the new width and height
        print(f'Resizing {filename}...')
        im = im.resize((width, height)) # resize takes a tuple, hence the double sets of parentheses
    
    # add the logo
    print(f'Adding logo to {filename}...')
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm) # the 3rd argument is a mask for transparency
    # if you didn't include logoIm as the mask in the 3rd argument, logoIm's transparent pixels would paste as white
    # save changes
    im.save(os.path.join('withLogo', filename))
