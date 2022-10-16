
"""
This project  will enable you to play the game of sliders. 
The objective of this game is to form the board so that all the numbers are ordered on the board. 
Usually, there is an empty block that will let you move blocks around, but we used number 0 for this purpose.
"""

import random

#This function generates a board with parameters which taken row and column.
def generate(row, column):
    if 10 >= row and column >1:
        matrix = []
        
        for i in range(row):          
            a =[]
            for j in range(column):     
                 a.append((i*row + j))  
            matrix.append(a)
          
        for i in range(row):
            for j in range(column):
                return matrix
    else: 
        return "The board matrix elements must be [0:1:(row*column-1)]"

#This function will make times random shuffles on a given board.
def shuffle(board, times=20):
    hareketler = []
    while True:
        for i in range(times): 
            movedirection = []
            if move_right(board) == 1:
                movedirection.append("R")
                move_left(board)
            if move_left(board) == 1:
                movedirection.append("L")
                move_right(board)
            if move_up(board) == 1:
                movedirection.append("U")
                move_down(board)
            if move_down(board) == 1:
                movedirection.append("D")
                move_up(board)
                
            hareket = random.choice(movedirection)
            
            if hareket == "R":
                move_right(board)
                hareketler.append("R")
            if hareket == "L":
                move_left(board)
                hareketler.append("L")
            if hareket == "U":
                move_up(board)
                hareketler.append("U")
            if hareket == "D":
                move_down(board)
                hareketler.append("D")
        if is_solved(board) == True:
            hareketler = []
            continue
        else:
            return hareketler
        
#This function will reset the board to the original form (solved form).       
def reset(board):  
    row= len(board)
    column= len(board[0])
    
    
    for i in range(row):
        for j in range(column):
            board[i][j] = i*row + j
    
    return None

#This function will take the board and check to see if the numbers within the board are valid, meaning, if all the numbers are unique and less than row x column. 
def is_valid(board):
    s=[]
    count=0
    row= len(board)
    column= len(board[0])
    x = True
    for i in board:
        for j in i:
            if j not in s:
                s.append(j)
                count+=1
    if count == (row*column):
        for i in s:
            if i >= row*column:
                x = False
    else:
        x = False
    return x

#This function will check if the board is solved.   
def is_solved(board):
    row = len(board)
    column = len(board[0])
    matrix = []
        
    for i in range(row):          
        a =[]
        for j in range(column):     
             a.append((i*row + j))  
        matrix.append(a)
      
    for i in range(row):
        for j in range(column):
            a = matrix
    
    if matrix == board:
        return True
    
    else:
        return False
    
#This function will take the board and return the size of the board as a tuple.
def get_board_size(board):
    row = len(board)
    column = len(board[0])
    size = (row, column)
    return size
    
#This function will swap the number 0 with the number to its right if it is possible meaning if there is a number to its right.   
def move_right(board):
    for row in board:
        for i in range(len(row) - 1):
            if(row[i] == 0):
                row[i] = row[i+1]
                row[i+1] = 0
                return 1
    return 0

#This function will swap the number 0 with the number to its left if it is possible meaning if there is a number to its left.    
def move_left(board):
    for row in board:
        for i in range(1,len(row)):
            if(row[i] == 0):
                row[i] = row[i-1]
                row[i-1] = 0
                return 1
    return 0

#This function will swap the number 0 with the number to its up if it is possible meaning if there is a number to its up.
def move_up(board):
    for row_no in range(1,len(board)):
        for column_no in range(len(board[row_no])):
                if(board[row_no][column_no] == 0):
                    board[row_no][column_no] = board[row_no - 1][column_no]
                    board[row_no - 1][column_no] = 0
                    return 1
    return 0

#This function will swap the number 0 with the number to its down if it is possible meaning if there is a number to its down.
def move_down(board):
    for row_no in range(len(board) - 1):
        for column_no in range(len(board[row_no])):
                if(board[row_no][column_no] == 0):
                    board[row_no][column_no] = board[row_no + 1][column_no]
                    board[row_no + 1][column_no] = 0
                    return 1
    return 0

#This function will swap the number 0 with one of its neighbors randomly.            
def move_random(board):
    movedirection = []
    if move_right(board) == 1:
        movedirection.append("R")
        move_left(board)
    if move_left(board) == 1:
        movedirection.append("L")
        move_right(board)
    if move_up(board) == 1:
        movedirection.append("U")
        move_down(board)
    if move_down(board) == 1:
        movedirection.append("D")
        move_up(board)
    hareket = random.choice(movedirection)
    if hareket == "R":
        move_right(board)
        return "R"
    if hareket == "L":
        move_left(board)
        return "L"
    if hareket == "U":
        move_up(board)
        return "U"
    if hareket == "D":
        move_down(board)
        return "D"

#This function will swap the number 0 with the neighboring numbers according to the given moves string if it is possible.                    
def move(board, moves):
    count = 0
    for char in moves:
        if char == "R" or char == "r":
            if move_right(board) == 1:
                count += 1
        if char == "L" or char == "l":
            if move_left(board) == 1:
                count += 1
        if char == "U" or char == "u":
            if move_up(board) == 1:
                count += 1
        if char == "D" or char == "d":
            if move_down(board) == 1:
                count += 1
    return count

#This function will rotate the whole board to the right (90° rotate), and return the new board.
def rotate(board):
    new_board = []
    for i in range(len(board[0])):
        l = list(map(lambda x: x[i], board))
        l.reverse()
        new_board.append(l)
    return new_board

#This function will print the given board on the console as a 2D matrix
def print_board(board):
    row = len(board)
    column = len(board[0])
    for i in range(row):
        for j in range(column):
            print(board[i][j], end = " ")
        print()

#This function will take a board,and a list of moves, then apply the given moves to the board and check after each move if the board is solved.
def play(board, moves):
    if is_valid(board) == False:
        return int("-2")
    if is_solved(board) == True:
        return 0
    else:
        hareketler = []
        while True:
            for char in moves:
                if char == "R" or char == "r":
                    if move_right(board) == 1:
                        hareketler.append(char)
                        if is_solved(board) == True:
                            return hareketler
                if char == "L" or char == "l":
                    if move_left(board) == 1:
                        hareketler.append(char)
                        if is_solved(board) == True:
                            return hareketler
                if char == "U" or char == "u":
                    if move_up(board) == 1:
                        hareketler.append(char)
                        if is_solved(board) == True:
                            return hareketler
                if char == "D" or char == "d":
                    if move_down(board) == 1:
                        hareketler.append(char)
                        if is_solved(board) == True:
                            return hareketler
        
            return int("-1")

#This function will be used to play the game by yourself using manual inputs.     
def play_interactive(board=None):
    if board == None:
        print("Please type the board size number:\n")
        row = int(input("Row number: "))
        column = int(input("Column number: "))
        board = generate(row,column)
        shuffle(board,)
    if is_valid(board) == False:
        a = ["",-2]
        return tuple(a)
    if is_solved(board) == True:
        print("This board is already solved.")
        return None
    hareketler= []
    count = 0
    print_board(board)
    while True:
        move= input(("Please type to move (Left: L, Right: R, Up: U, Down: D, Random: M) \nPress (q) to quit. :"))
        if move == "R" or move == "r":
            if move_right(board) == 1:
                    count += 1
                    hareketler.append("R")
                    print_board(board)
        if move == "L" or move == "l":
            if move_left(board) == 1:
                    count += 1
                    hareketler.append("L")
                    print_board(board)
        if move == "U" or move == "u":
            if move_up(board) == 1:
                    count += 1
                    hareketler.append("U")
                    print_board(board)
        if move == "D" or move == "d":
            if move_down(board) == 1:
                    count += 1
                    hareketler.append("D")
                    print_board(board)
        if move == "M" or move == "m":
            move_random(board)
            count += 1
            hareketler.append(move)
            print_board(board)
        
        if move == "Q" or move == "q":
            if is_solved(board) == True:
                a = [hareketler,count]
                return tuple(a)
            else:
                a = [hareketler, -1]
                return tuple(a)
            
        if is_solved(board) == True:
            a = [hareketler,count]
            return tuple(a)