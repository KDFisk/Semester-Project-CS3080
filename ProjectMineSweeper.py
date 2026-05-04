#Dean Fisk
#Semester Project: Minesweeper
#5/3/2026

import random

board = [
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' '],
    [' ', ' ', ' ',' ', ' ', ' ', ' ']]
#7x8 board with 10 mines

safe_spots = [(0,0), (0,1), (1,0), (1,1)]

for i in range (8):
    for j in range(7):
        if random.randint(0, 1) == 1:
            board[i][j] = 'mine '
        else:
            board[i][j] = 'safe '
        if (i, j) in safe_spots:
            board[i][j] = 'safe '

#Filling of the board with mines and safe spots, ensuring that the top-left corner is safe

    
class tracker():
    def __init__(self):
        self.board = board
    def check_spot(self, x, y):
        if self.board[x][y] == 'mine ':
            print("You lose!")
        else:
            print("You are safe!")
    def surrounding_mines(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (x+i) >= 0 and (x+i) < 8 and (y+j) >= 0 and (y+j) < 7:
                    if self.board[x+i][y+j] == 'mine ':
                        count += 1
        print(f"There are {count} mines surrounding this spot.")
