# Init
# %%
import numpy as np

with open("input.txt","r") as f:
    move_list =f.read().splitlines()

# A
# %%
h, d = 0, 0

for move in move_list:
    dir = move.split()[0]
    length = int(move.split()[1])

    if dir == "forward":
        h += length
    if dir == "down":
        d += length
    if dir == "up":
        d -= length

answer = h*d    

# %%
submit(answer)


# B
# %%
h, d, a = 0, 0, 0

for move in move_list:
    dir = move.split()[0]
    length = int(move.split()[1])

    if dir == "forward":
        h += length
        d += a*length
    if dir == "down":
        a += length
    if dir == "up":
        a -= length

answer = h*d    

answer

# %%
submit(answer)
