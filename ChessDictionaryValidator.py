# Chapter 5 practice project #1
# a program to determine whether or not a chessboard is valid

# valid chess pieces: wking, wqueen, wbishop, wknight, wrook, wpawn, bking, bqueen, bbishop, bknight, brook, bpawn
# valid chess board locations: 1a to 8h
# chessboard dictionary data structure: {location: piece}
# chessboard must have at least one of each king, no more than one of each queen,
# no more than two of each other main piece, and no more than 8 pawns

# This function is the heart of this program
# Function that takes a chessboard data structure and returns true or False

def isValidChessboard(chessboard):

    # First, check that each side has a king, and if not, return False
    if ('wking' not in chessboard.values()) or ('bking' not in chessboard.values()):
        print('ERROR: Missing a King')
        return False

    # Next, loop through the pieces to check they are among the valid pieces and to count them
    # set all of the counts to zero
    blackPieces = 0
    whitePieces = 0
    pieces_counts = {'wking': 0, 'wqueen': 0, 'wbishop': 0, 'wknight': 0, 'wrook': 0, 'wpawn': 0,
                     'bking': 0, 'bqueen': 0, 'bbishop': 0, 'bknight': 0, 'brook': 0, 'bpawn': 0}

    # the keys for the above also define the valid pieces

    # loop through all of the pieces in the chessboard
    for piece in chessboard.values():
        # Check that it's a valid piece
        if piece not in pieces_counts.keys():
            print('ERROR: ' + piece + ' is not a valid chess piece for this board.')
            return False
        # Count and validate the total numbers of black and white pieces
        if piece[0] == 'w':
            whitePieces += 1
            if whitePieces > 16:
                print('ERROR: Too many white pieces')
                return False
        elif piece[0] == 'b':
            blackPieces += 1
            if blackPieces > 16:
                print('ERROR: Too many black pieces')
                return False
        # Count the numbers of each piece
        pieces_counts[piece] += 1

    # Check that any count hasn't exceeded a valid count
    if (pieces_counts['wking'] > 1) or (pieces_counts['bking'] > 1):
        print('ERROR: Too many kings')
        return False
    elif (pieces_counts['wqueen'] > 1) or (pieces_counts['bqueen'] > 1):
        print('ERROR: Too many queens')
        return False
    elif (pieces_counts['wbishop'] > 2) or (pieces_counts['bbishop'] > 2):
        print('ERROR: Too many bishops')
        return False
    elif (pieces_counts['wknight'] > 2) or (pieces_counts['bknight'] > 2):
        print('ERROR: Too many knights')
        return False
    elif (pieces_counts['wrook'] > 2) or (pieces_counts['brook'] > 2):
        print('ERROR: Too many rooks')
        return False
    elif (pieces_counts['wpawn'] >8 ) or (pieces_counts['bpawn'] > 8):
        print('ERROR: Too many pawns')
        return False

    #Finally, check that the pieces are only on valid locations on the chessboard
    validColumns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    validRows = ['1', '2', '3', '4', '5', '6', '7', '8']
    for location in chessboard.keys():
        if (location[0] not in validRows) or (location[1] not in validColumns):
            print('ERROR: ' + location + ' is not a valid position for ' + chessboard[location])
            return False


    #If all of the above conditions not returned False, the chessboard is valid
    print('This chessboard checks out.')
    return True

#MARK: end of isValidChessboard(chessboard) function

testBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
errorPositionBoard = {'1i': 'bking', '8h': 'wking'}
errorMissingKing = {'2f': 'bking', '8a': 'wrook'}
errorTooManyBishops = {'1e': 'wking', '8e': 'bking', '1d': 'wqueen', '8d': 'bqueen', '8c': 'bbishop', '8f': 'bbishop', '7e': 'bbishop'}

isValidChessboard(testBoard)
isValidChessboard(errorPositionBoard)
isValidChessboard(errorMissingKing)
isValidChessboard(errorTooManyBishops)
