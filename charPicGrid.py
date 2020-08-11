# Character Picture Grid practice project, pg. 108

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Create a program to take the above grid and print a version rotated 90 degrees to show an ascii heart

for y in range(len(grid[0])):
    for x in range(len(grid)):
        print(grid[len(grid) - 1 - x][y], end='') #print each character subsequently
    print() # go to a new line after printing all of the characters in a line





