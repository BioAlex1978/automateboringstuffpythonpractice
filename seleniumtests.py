from selenium import webdriver
# the following doesn't work in Thonny for some reason; instead have to pass full path to webdriver.Chrome()
#browser = webdriver.Chrome()
browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('cover-thumb')
    print(f'Found {elem.tag_name} with that class name!')
    
    linkElem = browser.find_element_by_link_text('Read Online for Free')
    type(linkElem)
    print('clicking link')
    linkElem.click()
except:
    print('Was not able to find an element with that name.')
