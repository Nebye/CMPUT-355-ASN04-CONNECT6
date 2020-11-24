# Just in case I don't get the othello viz/player working on time, I'm going to make this
# This is a viz for Connect6 (which is a valid game for the CGO games comp so it should be valid for this assignment)

import math
import numpy as np
# import random




def play(move):
    if (move == 0):
        player = 'black'
    else:
        player = 'white'
    
        
    loc_x, loc_y = input("What is your play "+player+" [format:xy]: ").split()
    
    # swap these with try except handlers
    while(len() != 2):
        print("Invalid input!")
        loc_x, loc_y = input("What is your play "+player+" [format:xy]: ").split()
    
    while(board[loc_x][loc_y] != '*'):
        print("Invalid input!")
        loc_x, loc_y = input("What is your play "+player+" [format:xy]: ").split()

    counter = 0
    
    board[0][1] = 2
    
    # prints current board/grid/game
    for board_size in board:
        print(board_size)
    
        
    # check if anyone has won
    
def main():
    # first = random.randint(0,1) # 0 is black and 1 is white
    # according to rules black always plays first
    first = 0
    
    global board # init grid
    global board_size # init dimensions for grid
    
    board_size = int(input("What is your board size (min of 19): "))
    while(board_size < 19):
        board_size = int(input("What is your board size (min of 19): "))
        
    board = [[0 for i in range(board_size)] for j in range(board_size)]
    play(first)
    

main()