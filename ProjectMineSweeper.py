#Dean Fisk
#Semester Project: Minesweeper
#5/3/2026

from itertools import count
import random

class tracker():
    def __init__(self):
        self.board = board
        self.user_board = user_board
        
    def check_spot(self, x, y):
        if self.board[x][y] == 'mine ':
            self.user_board[x][y] = 'mine '
            print("You lose!")
            return 1
        else:
            self.user_board[x][y] = 'safe '
            print("You are safe!")
            return 0
            
    def surrounding_mines(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (x+i) >= 0 and (x+i) < 8 and (y+j) >= 0 and (y+j) < 7:
                    if self.board[x+i][y+j] == 'mine ':
                        count += 1
        return count
    
    def win_condition(self, x, y):
        if (x, y) == (7,6):
            print("Final guess, is this a mine? (y/n)")
            if input() == 'y' and self.board[7][6] == 'mine ':
                print("You win!")
                return True
            elif input() == 'n' and self.board[7][6] == 'safe ':
                print("You win!")
                return True
            else:   
                print ("You lose!")
                return False
                    
#Creating the tracker class that will be used to check if a spot is a mine and to count the number of surrounding mines

board = [
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' ']]
#7x8 board 
user_board = [
    ['safe ', 'safe ', ' ',' ', ' ', ' ', ' '],
    ['safe ', 'safe ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' ']]

safe_spots = [(0,0), (0,1), (1,0), (1,1)]

for i in range (8):
    for j in range(7):
        if random.randint(0, 3) == 0:
            board[i][j] = 'mine '
        else:
            board[i][j] = 'safe '
        if (i, j) in safe_spots:
            board[i][j] = 'safe '

#Filling of the board with mines and safe spots, ensuring that the top-left corner is safe

GameTracker = tracker()
GameContinue = True

startCoords = [(0, 1), (1, 0), (1, 1)]
for k,j in startCoords:
        mines_surround = GameTracker.surrounding_mines(k, j)
        print(f"There are {mines_surround} mines surrounding this spot {k,j}.")

while GameContinue:
    x = int(input("Enter the x (row) coordinate of the spot you want to check (0-7): "))
    y = int(input("Enter the y (column) coordinate of the spot you want to check (0-6): "))
    check_Mine = GameTracker.check_spot(x, y)
    if check_Mine == 1:
        GameContinue = False
        for row in board:
            print(row)
        break
    #checking if spot is a mine, if it is the game ends and shows the board, if not it continues
    
    mines_surround = GameTracker.surrounding_mines(x, y)
    print(f"There are {mines_surround} mines surrounding this spot ({x}, {y}).")
    for row in user_board:
        print(row)
    #Giving the user feedback on how many mines are surrounding the spot they checked and showing the user board after each turn
    
    if GameTracker.win_condition(x, y):
        GameContinue = False
        for row in user_board and board:
            print(row)
        print("Congratulations on winning the game!")
    #Checking if the user has won the game, if they have it ends and shows the user board and the actual board
