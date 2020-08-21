#! python3

# spiralDraw.py - a simple program to take control of the mouse and draw a square spiral
# in the window of a drawing app. When run, the user has 5 seconds to position the mouse
# cursor over the window of a drawing app, and the script will do the rest
# Automate the Boring Stuff with Python 2e, Ch.20, pg.479

# NOTE: though the book says the drag() function defaults to left button, this wouldn't work
# until I explicitly included it as an argument

import pyautogui, time

time.sleep(5) # wait 5 seconds
pyautogui.click() # click to make the window under the mouse active

distance = 300
change = 20

while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2, button='left') # move right
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.2, button='left') # move down
    pyautogui.drag(-distance, 0, duration=0.2, button='left') # move left
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.2, button='left') # move up
