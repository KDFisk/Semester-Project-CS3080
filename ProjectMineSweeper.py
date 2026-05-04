#Dean Fisk
#Semester Project: Minesweeper
#5/3/2026

from itertools import count
import random
minecount = 25

class tracker():
    def __init__(self):
        self.board = board
        self.user_board = user_board
        
        
    def check_spot(self, x, y):
        if self.board[x][y] == 'mine ':
            self.user_board[x][y] = 'mine'
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
    
    def win_condition(self, counter):
        if counter == 0:
            return True
        else:
            counter -= 1
            return False
        

board = [
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' ']]
#8x7 board 
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
mines_placed = 0

for i in range (8):
    for j in range(7):
        randomint = random.randint(0, 2)
        
        if randomint == 0 and minecount > 0:
            board[i][j] = 'mine '
            minecount -= 1
            mines_placed += 1
        else:
            board[i][j] = 'safe '
        if (i, j) in safe_spots:
            board[i][j] = 'safe '

#Filling of the board with mines and safe spots, ensuring that the top-left corner is safe

GameTracker = tracker()
GameContinue = True
GuessHistory = [(0, 0), (0, 1), (1, 0), (1, 1)]

startCoords = [(0, 1), (1, 0), (1, 1)]
for k,j in startCoords:
        mines_surround = GameTracker.surrounding_mines(k, j)
        print(f"There are {mines_surround} mines surrounding this spot {k,j}.")

while GameContinue:
    x = int(input("Enter the x (row) coordinate of the spot you want to check (0-7): "))
    y = int(input("Enter the y (column) coordinate of the spot you want to check (0-6): "))
    if x < -1 or x > 8 or y < 0 or y >= 7:
        print("Invalid coordinates. Please enter coordinates within the board boundaries.")
        continue

    counter = 8*7 - mines_placed - 4
    if GameTracker.win_condition(counter):
        GameContinue = False
        for row in user_board and board:
            print(row)
        print("Congratulations on winning the game!")
    #Checking if the user has won the game, if they have it ends and shows the user board and the actual board
    
    if (x, y) in GuessHistory:
        print("You have already checked this spot, please choose a different one.")
        continue
    GuessHistory.append((x, y))
    
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
    

