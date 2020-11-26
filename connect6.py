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
    
    while True:
        try:
            loc_x, loc_y = input("What is your play "+player+" [format:row column]: ").split()
            loc_x = int(loc_x)
            loc_y = int(loc_y) 
            if (board[int(loc_x)][int(loc_y)] != 7):
                raise ValueError
            break
        except ValueError:
            print("Invalid input!")        

    
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
    horizontal = board[loc_x]
    #print("hor")
    #print(horizontal)
    
    # vertical
    vertical = []
    count = 0
    while (count < board_size):
        vertical.append(board[count][loc_y])
        count = count +1
    #print("vert")
    #print(vertical)
    
    
    
    
    
    diagonal01 = [] # for diagonal positive down →↓
    index = 0
    while ((loc_x + index < board_size) and (loc_y + index < board_size)): # either hit row 19 or col 19
        tile = board[loc_x + index][loc_y + index]
        diagonal01.append(tile)
        index = index +1
    #print("diagonal01")
    #print(diagonal01)
    
    diagonal02 = [] # for diagonal negative up ←↑ 
    index = 1 # start at 1 as to exclude the current move - it was already included in diagonal01
    while ((loc_x - index > -1) and (loc_y - index > -1)): # either hit row 0 or col 0
        tile = board[loc_x - index][loc_y - index]
        diagonal02.append(tile)
        index = index +1    
    #print("diagonal01")
    diagonal02.reverse() # reverse as to make it align with the direction of the first diagonal
    #print(diagonal02)    
    
    diagonalPrime01 = [] # combines diagonal01 and diagonal02
    diagonalPrime01.extend(diagonal02) # insert to the first half of the first diagonal
    diagonalPrime01.extend(diagonal01)
    #print("DiagonalPrime01")
    #print(diagonalPrime01)  
    
    
    
    
    
    diagonal03 = [] # for diagonal positive up →↑
    index = 1
    while ((loc_x - index > -1) and (loc_y + index < board_size)): # either hit row 0 or col 19
        tile = board[loc_x - index][loc_y + index]
        diagonal03.append(tile)
        index = index + 1
    #print("diagonal03")
    #print(diagonal03)
    
    diagonal04 = [] # for diagonal negative down ←↓
    # either hit row 19 or col 0
    index = 0
    while ((loc_x + index < board_size) and (loc_y - index > -1)): # either hit row 19 or col 0
        tile = board[loc_x + index][loc_y - index]
        diagonal04.append(tile)
        index = index + 1
    #print("diagonal04")
    #print(diagonal04)    
    
    
    diagonal04.reverse() # reverse as to make it align with the direction of the first diagonal   
    
    diagonalPrime02 = [] # combines diagonal01 and diagonal02
    diagonalPrime02.extend(diagonal04) # insert to the first half of the first diagonal
    diagonalPrime02.extend(diagonal03)
    #print("DiagonalPrime02")
    #print(diagonalPrime02)      
    

    # Win Check
    if move == 0:
        b = [0] * 6
    else:
        b = [1] * 6
    if (is_Sublist(diagonalPrime01, b) == True or is_Sublist(diagonalPrime02, b) == True or is_Sublist(horizontal, b) == True or is_Sublist(vertical, b) == True):
        win = True
    else:
        win = False
    

    
    
    if move == 0:
        move = 1
    else:
        move = 0    
        
    if(win == True): # replace with check to see if anyone won
        print(player, "wins!")
        while True:
            try:        
                play_again = str(input("Would you like to play again [Y/N]?"))
                if (play_again != "Y" and play_again != "N"):
                    raise ValueError
                break
            except ValueError:
                print("Invalid Response")      
        if(play_again == "Y"):
            main()
        else:
            sys.exit()      
    else:
        play(move)
    
    

def is_Sublist(lst1, lst2):
    ls1 = [element for element in lst1 if element in lst2]
    ls2 = [element for element in lst2 if element in lst1]
    return ls1 == ls2


def main():
    # first = random.randint(0,1) # 0 is black and 1 is white
    # according to rules black always plays first
    first = 0
    
    global board # init grid
    global board_size # init dimensions for grid
    
    print("Welcome to Connect6")
    while True:
        try:
            board_size = int(input("What is your board size (min of 19): "))
            if(board_size < 19):
                raise ValueError
            break
        except ValueError:
            print("Invalid Response") 
        
    board = [[7 for i in range(board_size)] for j in range(board_size)]
    play(first)
    
    
main()