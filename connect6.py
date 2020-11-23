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
        
    location = input("What is your play "+player+" [format:x y]: ") 
    
    #while(location != valid):
        #location = input("Invalid move, please try again: ")
    #    pass

    counter = 0
    for i in range(board_size):
        if counter == 0:
            for x in range(0, board_size+1):
                print(x, end=" ") 
            print("\n")
        counter = counter + 1 
        print(counter, "* "*board_size)
        
    # check if anyone has won
    
def main():
    # first = random.randint(0,1) # 0 is black and 1 is white
    # according to rules black always plays first
    first = 0
    
    global board_size
    board_size = int(input("What is your board size (min of 19): "))
    while(board_size < 19):
        board_size = int(input("What is your board size (min of 19): "))
    play(first)
    

main()