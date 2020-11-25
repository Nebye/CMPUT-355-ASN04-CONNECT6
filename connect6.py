"""
Just in case I don't get the othello viz/player working on time, I'm going to make this
This is a viz for Connect6 (which is a valid game for the CGO games comp so it should be valid for this assignment)

TODO
- Check for matches horizontal
- Check for matches vertical
- Check for matches diagonal

- General Clean Up - maybe put into separate functions
- General Clean Up - Fix/make more error checks

"""
import sys
import math
import numpy as np
# import random




def play(move):
    if (move == 0):
        player = 'black'
    else:
        player = 'white'
    
        
    loc_x, loc_y = input("What is your play "+player+" [format:row column]: ").split()
    loc_x = int(loc_x)
    loc_y = int(loc_y)
    
    # swap these with try except handlers
    while(board[int(loc_x)][int(loc_y)] != 7):
        print("Invalid input!")
        loc_x, loc_y = input("What is your play "+player+" [format:row column]: ").split()

    
    
    board[loc_x][loc_y] = move
    
    # Viewing current board/grid/game 
    
    # prints col numbers
    #for i in range(0, len(board[0])): 
    #    print(i, end=" ")    
    #print("\n")    
    
    #col_num = 0
    for i in board:
        print(i)
        #prints row numbers
        #print(col_num, i)
        #col_num = col_num + 1
        
    
    
        
    # check if the current player has made a winning move
    # horizontal
    # vertical
    
    # diagonal 01 (SE)
    diagonal01 = [] # for diagonal positive down →↓
    index = 0
    while (index < board_size-loc_x-1 or index < board_size-loc_y-1):
        tile = board[loc_x + index][loc_y + index]
        diagonal01.append(tile)
        index = index +1
    print("diagonal01")
    print(diagonal01)
    
    diagonal02 = [] # for diagonal negative up ←↑ 
    index = 1 # start at 1 as to exclude the current move - it was already included in diagonal01
    while (loc_x - index  > 0 or loc_y - index  > 0):
        tile = board[loc_x - index][loc_y - index]
        diagonal02.append(tile)
        index = index +1    
    print("diagonal01")
    diagonal02.reverse() # reverse as to make it align with the direction of the first diagonal
    print(diagonal02)    
    
    diagonalPrime01 = [] # combines diagonal01 and diagonal02
    diagonalPrime01.extend(diagonal02) # insert to the first half of the first diagonal
    diagonalPrime01.extend(diagonal01)
    print(diagonalPrime01)  
    
    diagonal03 = [] # for diagonal positive up →↑
    
    
    diagonal04 = [] # for diagonal negative down ←↓
    
    #print(diagonal01)
    #print(diagonal02)
    """
    [0][1]
    
    [1][2]
    
    [3][2]
    [4][3]
    [5][4]
    [6][5]
    ...
    [8][9] either going to get to final x or y
    """
    
    # diagonal 02 (SW)
    
    
    
    
    if move == 0:
        move = 1
    else:
        move = 0    
        
    if(move == 8): # replace with check to see if anyone won
        print(player, "wins!")
        play_again = str(input("Would you like to play again [Y/N]?"))
        if(play_again == "Y"):
            main()
        else:
            sys.exit()            
    else:
        play(move)
    
def main():
    # first = random.randint(0,1) # 0 is black and 1 is white
    # according to rules black always plays first
    first = 0
    
    global board # init grid
    global board_size # init dimensions for grid
    
    print("Welcome to Connect6")
    board_size = int(input("What is your board size (min of 19): "))
    while(board_size < 10):
        board_size = int(input("What is your board size (min of 19): "))
        
    board = [[7 for i in range(board_size)] for j in range(board_size)]
    play(first)
    

main()