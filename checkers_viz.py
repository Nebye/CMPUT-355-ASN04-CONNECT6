# Just in case I don't get the othello viz/player working on time, I'm going to make this
# This is a viz for Checkers (which is a valid game for the CGO games comp so it should be valid for this assignment)

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
    #    location = input("Invalid move, please try again: ")
        
    board(location)

def board(last_play):
    for i in range(board_size):
        print("* "*board_size)
        
    # check if anyone has won
    
    
def main():
    first = random.randint(0,1) # 0 is black and 1 is white
    
    first = 0
    play(first)
    

main()