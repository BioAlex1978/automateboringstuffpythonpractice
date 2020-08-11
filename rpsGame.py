# A simple 'Rock, Paper, Scissors' game from "Automate the Boring Stuff with Python, 2nd Edition", pg.52

# First, I will attempt to do this on my own based on what I've learned so far
# Then, below that, I will add the book's version.
# Import statements will be the same for both, so I'll just add the import here:

import random, sys

# My attempt, based on the sample output shown on pg.51
# NOTE: My version uses lists, which this book hasn't introduced, but I was familiar with from another book

wins = 0
losses = 0
ties = 0
moves = ['r', 'p', 's'] # list of moves, from which we can get an index number for the player's move
moveNames = ['ROCK', 'PAPER', 'SCISSORS'] # list of move names for displaying the computer's and player's moves using their indices

print('ROCK, PAPER, SCISSORS') # display the title at the start of the game

while True:
    computerMoveIndex = random.randint(0, 2) # first the computer's move is chosen as a random integer from 0 to 2

    print(str(wins) + ' wins, ' + str(losses) + ' losses, ' + str(ties) + ' ties.')
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    yourMove = input()
    if yourMove == 'q': # first, see if the player is quitting the game, and if so, exit
        print('Thank you for playing!')
        sys.exit()
    elif not ((yourMove == 'r') or (yourMove == 'p') or (yourMove == 's')): # then, double check that the player is choosing a valid option, and if not, restart the loop
        print(yourMove + ' is not a valid choice. Please try again with r, p, s, or q!')
        continue
    else:
        yourMoveIndex = moves.index(yourMove) # finally, if the player has made a valid choice, get the index of that move from the moves list
    print(moveNames[yourMoveIndex] + ' versus...')
    print(moveNames[computerMoveIndex])

    # Check to see if it's a win, loss, or tie
    if yourMoveIndex == computerMoveIndex: #first check for a tie, as it's the simplest to evaluate
        print('It is a tie!')
        ties += 1
        continue

    if computerMoveIndex == 0: # next, evaluate if computer has chosen ROCK
        if yourMoveIndex == 1:
            print('You win!')
            wins += 1
            continue
        elif yourMoveIndex == 2:
            print('You lose!')
            losses += 1
            continue
        else:
            print('If you are seeing this message, something is wrong. This condition should never happen')

    if computerMoveIndex == 1: # next, evaluate if computer has chosen PAPER
        if yourMoveIndex == 2:
            print('You win!')
            wins += 1
            continue
        elif yourMoveIndex == 0:
            print('You lose!')
            losses += 1
            continue
        else:
            print('If you are seeing this message, something is wrong. This condition should never happen')

    if computerMoveIndex == 2: # next, evaluate if computer has chosen SCISSORS
        if yourMoveIndex == 0:
            print('You win!')
            wins += 1
            continue
        elif yourMoveIndex == 1:
            print('You lose!')
            losses += 1
            continue
        else:
            print('If you are seeing this message, something is wrong. This condition should never happen')

# This is the book's version. It doesn't use lists, but I think it does a better job of using if statements
# to check the game outcomes. Since there are only a few possible combinations, it uses a pattern of
# "if playerMove == X and computerMove == Y:" to evaluate all possibilities quickly, rather than the
# nested if statements I did for each possible computerMove


#print('ROCK, PAPER, SCISSORS')
#
## These variables keep track of the numbers of wins, losses, and ties
#wins = 0
#losses = 0
#ties = 0
#
#while True: # the main game loop
#	print('%s Wins, %s Looses, %s Ties' % (wins, losses, ties))
#	while True: # player input loop
#		print('Enter your move: (r)ock (p)aper (s)scissors or (q)uit')
#		playerMove = input()
#		if playerMove == 'q':
#			sys.exit() # quit the program
#		if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
#			break # break out of the player input loop
#		print('Type one of r, p, s, or q.')
#	
#	# Display what the player chose:
#	if playerMove == 'r':
#		print('ROCK versus...')
#	elif playerMove == 'p':
#		print('PAPER versus...')
#	elif playerMove == 's':
#		print('SCISSORS versus...')
#	
#	# Display what the computer chose:
#	randomNumber = random.randint(1, 3)
#	if randomNumber == 1:
#		computerMove = 'r'
#		print('ROCK')
#	elif randomNumber == 2:
#		computerMove = 'p'
#		print('PAPER')
#	elif randomNumber == 3:
#		computerMove == 's'
#		print('SCISSORS')
#		
#	# Display and record the win/loss/tie
#	if playerMove == computerMove:
#		print('It is a tie!')
#		ties = ties + 1
#	elif playerMove == 'r' and computerMove == 's':
#		print('You win!')
#		wins = wins + 1
#	elif playerMove == 'p' and computerMove == 'r':
#		print('You win!')
#		wins = wins + 1
#	elif playerMove == 's' and computerMove == 'p':
#		print('You win!')
#		wins = wins + 1
#	elif playerMove == 'r' and computerMove == 'p':
#		print('You lose!')
#		losses = losses + 1
#	elif playerMove == 'p' and computerMove == 's':
#		print('You lose!')
#		losses = losses + 1
#	elif playerMove == 's' and computerMove == 'r':
#		print('You lose!')
#		losses = losses + 1
