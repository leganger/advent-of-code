# Init
# %%
import numpy as np
from aocd.models import Puzzle

# REMEMBER TO UPDATE DATE
puzzle = Puzzle(year=2021, day=3)

# A
# %%
data = puzzle.input_data.splitlines()

data_len = len(data)
gamma_bin = ""
epsilon_bin = ""

for col_idx, col in enumerate(data[0]):
    col_counter = 0
    for row in data:
        if row[col_idx] == "1":
            col_counter += 1
    g = str(round(col_counter/data_len + 1e-15))
    if g == "1":
        e = "0"
    else:
        e = "1"
    gamma_bin += g
    epsilon_bin += e


def str_to_bin(string: str) -> int:
    l = []
    for idx, i in enumerate(string[::-1]):
        if i == "1":
            l.append(2**idx)
    return sum(l)

gamma = str_to_bin(gamma_bin)
epsilon = str_to_bin(epsilon_bin)


answer = gamma*epsilon

# %%
puzzle.answer_a = answer

# B
# %%
def data_screen(data: list, epsilon: bool = False) -> int:

    gamma_bin = ""
    epsilon_bin = ""

    for col_idx, _ in enumerate(data[0]):
        new_data = []
        data_len = len(data)

        col_counter = 0
        for row in data:
            if row[col_idx] == "1":
                col_counter += 1
        g = str(round(col_counter/data_len + 1e-15))
        if g == "1":
            e = "0"
        else:
            e = "1"
        gamma_bin += g
        epsilon_bin += e

        print(gamma_bin, epsilon_bin)

        for row in data:
            if epsilon:
                if row[col_idx] == epsilon_bin[col_idx]:
                    new_data.append(row)
            else:
                if row[col_idx] == gamma_bin[col_idx]:
                    new_data.append(row)
        if len(new_data)==1:
            break
        data = new_data

    return str_to_bin(new_data[0]), new_data[0]

oxygen, oxygen_bin = data_screen(data)
scrubber, scrubber_bin = data_screen(data, epsilon=True)

answer = oxygen*scrubber

# %%
puzzle.answer_b = answer
# %%
