# %%
import numpy as np
from aocd.models import Puzzle

# REMEMBER TO UPDATE DATE
puzzle = Puzzle(year=2021, day=5)
dl = puzzle.input_data.splitlines()

test = """0,0 -> 3,3
3,0 -> 0,3
0,0 -> 3,0
2,2 -> 2,3
"""

#dl = test.splitlines()

# %%
map = np.zeros((999,999))

for line in dl:
    print(line)
    x1, y1 = [int(x) for x in line.split(" -> ")[0].split(",")]
    x2, y2 = [int(x) for x in line.split(" -> ")[1].split(",")]

    x_min = min(x1, x2)
    x_max = max(x1, x2)
    y_min = min(y1, y2)
    y_max = max(y1, y2)

    if x1==x2:
        map[x1][y_min:y_max+1] += 1
    elif y1==y2:
        map.T[y1][x_min:x_max+1] += 1

answer = np.sum(map>1)

# %%
puzzle.answer_a = answer

# %%
#map = np.zeros((999,999))

for line in dl:
    print(line)
    x1, y1 = [int(x) for x in line.split(" -> ")[0].split(",")]
    x2, y2 = [int(x) for x in line.split(" -> ")[1].split(",")]

    x_len = abs(x2-x1)
    y_len = abs(y2-y1)

    if ((x_len>0) & (y_len>0)):

        x_dir = int((x2-x1)/max(1,x_len))
        y_dir = int((y2-y1)/max(1,y_len))

        for x_step in range(x_len+1):
            map[x1 + x_dir*x_step][y1 + y_dir*x_step] += 1

answer = np.sum(map>1)
# %%
puzzle.answer_b = answer

# %%
