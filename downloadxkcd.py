#! python3
# downloadxkcd.py - Downloads every single xkcd comic

# NOTE: This would cause heavy traffic to xkcd and download a lot of data. For testing purposes,
# we'll set the start URL to comic #5 and only download 5 comics

import requests, os, bs4

#url = 'https://xkcd.com/' # starting URL; uncomment to get all xkcd comics, and comment out the next line
url = 'https://xkcd.com/5/' # for testing purposes to get only a few; comment this out & uncomment above to get them all
os.makedirs('xkcd', exist_ok=True) # store the comics in ./xkcd
imgCount = 0 # to keep track of the number of comics downloaded
while not url.endswith('#'):
    # Download the page.
    print(f'Downloading page {url}...')
    res = requests.get(url) # get the URL as a response object
    res.raise_for_status() # raises an exception and ends the script of URL is bad
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser') #uses the html.parser to create a soup object of all the markup & styles
    
    # Find the URL of the comic image
    # On xkcd, the comic img tag is in a div with ID "comic", so the CSS selector to find it is #comic
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicURL = 'https:' + comicElem[0].get('src')
        # Download the image
        print(f'Downloading image {comicURL}...')
        comicRes = requests.get(comicURL)
        comicRes.raise_for_status()
    
    
        # Save the image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
        for chunk in comicRes.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    
    # Get the Prev button's URL.
    # gets the object containing anchor w/ link to the previous comic
    # the 0 index gets all elements of the anchor tags and content
    prevLink = soup.select('a[rel="prev"]')[0] 
    # update the value of url to the previous comic page using prevLink's href attribute value
    url = 'https://xkcd.com' + prevLink.get('href')
    
    # Update the image count.
    imgCount += 1

print(f'Done. {imgCount} comics downloaded.')