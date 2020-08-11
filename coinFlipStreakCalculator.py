# Coin Flip Streaks practice project on pg. 107
# This program checks if and how often a streak of 6 heads or tails occurs in a trial of 100 coin flips
# First, 'flip a coin' 100 times. Then check for streaks. Finally, tally the streaks over 10k iterations & calculate the frequency

import random

# global properties
numberOfStreaks = 0 # Total number of streaks recorded
iterations = 10000 # number of iterations for the experiment
flips = 100 # number of coin flips per iteration
streakLength = 6 # length of a streak to be tested
atLeastOneStreak = 0 # number of iterations containing at least one streak


# flip a coin 100 times, return a string of H and T to represent the flips
def coinFlip():
    flipTally = []
    for flip in range(flips):
        if random.randint(0, 1) == 1:
            # record heads
            flipTally.append('H')
        else:
            # record tails
            flipTally.append('T')

    flipString = ''.join(flipTally)
    return flipString

# record the number of Streaks in a coin flip string
def countStreaks(flipString):
    headsStreakCount = flipString.count('H' * streakLength)
    tailsStreakCount = flipString.count('T' * streakLength)
    return headsStreakCount + tailsStreakCount

# Loop to run the experiment
for iteration in range(iterations):
    streaksThisRound = countStreaks(coinFlip())
    if bool(streaksThisRound):
        atLeastOneStreak += 1
    numberOfStreaks += streaksThisRound

#Display the results
print('Chance of at least one streak of 6 Heads or 6 Tails occuring in a trial of %s flips: %s%%.' % (flips, (100 * atLeastOneStreak / iterations)))
print('Frequency of streaks among the total number of flips: %s' % ((numberOfStreaks / (iterations * flips))))

