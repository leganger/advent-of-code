# Init
# %%
import numpy as np
from aocd.models import Puzzle

# REMEMBER TO UPDATE DATE
puzzle = Puzzle(year=2021, day=4)

# A
# %%
data = puzzle.input_data.splitlines()
numbers = [int(x) for x in data[0].split(",")]

board_data = data[1:]

boards = []
for line_num, line in enumerate(board_data):
    if line == "":
        bl1 = [int(x) for x in board_data[line_num+1].strip().replace("  "," ").split(" ")]
        bl2 = [int(x) for x in board_data[line_num+2].strip().replace("  "," ").split(" ")]
        bl3 = [int(x) for x in board_data[line_num+3].strip().replace("  "," ").split(" ")]
        bl4 = [int(x) for x in board_data[line_num+4].strip().replace("  "," ").split(" ")]
        bl5 = [int(x) for x in board_data[line_num+5].strip().replace("  "," ").split(" ")]
        boards.append(np.array([bl1,bl2,bl3,bl4,bl5]))
boards = np.array(boards)

def mark_board(number, board):
    for r_idx, row in enumerate(board):
        for c_idx, col in enumerate(row):
            if col == number:
                board[r_idx][c_idx] = -1
    return(board)

def check_board(board):
    for row in board:
        if all(row<0):
            return True
    for  row in board.T:
        if all(row<0):
            return True
    return False

def score_board(number, board):
    board_sum = 0
    for row in board:
        for col in row:
            if col > 0:
                board_sum += col
    return number*board_sum


done = False
for number in numbers:
    for board_idx, board in enumerate(boards):
        boards[board_idx] = mark_board(number, board)
        if check_board(board):
            answer = score_board(number, board)
            done = True
            break
    if done:
        break

# %%
puzzle.answer_a = answer

# B
# %%
for number in numbers:
    new_boards = []
    for board in boards:
        marked_board = mark_board(number, board)
        if check_board(marked_board)==False:
            new_boards.append(marked_board)
    if len(boards)==1:
        if check_board(marked_board):
            answer = score_board(number,marked_board)
            break
    print(len(new_boards))
    boards = new_boards


# %%
puzzle.answer_b = answer
# %%
