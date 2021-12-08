# %%
import numpy as np
from aocd.models import Puzzle

# REMEMBER TO UPDATE DATE
puzzle = Puzzle(year=2021, day=9)
dl = puzzle.input_data.splitlines()


test = ["1234","2045","1234","1121","4563","3245"]
#dl = test
# %%
shape = len(dl), len(dl[0])

hmap = np.zeros(shape)
riskmap = np.zeros(shape)

def risk(hmap, x,y) -> int:
    depth = hmap[y][x]
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if ((dx == 0) & (dy == 0)):
                continue
            if ((dx == 1) & (dy == 1)):
                continue
            if ((dx == 1) & (dy == -1)):
                continue
            if ((dx == -1) & (dy == 1)):
                continue
            if ((dx == -1) & (dy == -1)):
                continue
            if all([x+dx >= 0, x+dx < hmap.shape[1], y+dy >= 0, y+dy < hmap.shape[0]]):
                if hmap[y+dy][x+dx] <= depth:
                    return 0
    risk = depth + 1
    return risk

for y,row in enumerate(dl):
    for x,col in enumerate(row):
        hmap[y][x] = col

for y,row in enumerate(dl):
    for x,col in enumerate(row):
        riskmap[y][x] = risk(hmap,x,y)

answer = int(np.sum(riskmap))

# %%
puzzle.answer_a = answer
# %%
def basin_size(hmap,X,Y):
    if risk(hmap,X,Y)>0:
        print(f"Found low point ({X},{Y})!")
        basin_points = [(X,Y)]
        new_basin_points = []
        scanned_list = []
        while True:
            for point in basin_points:
                if point not in new_basin_points:
                    new_basin_points.append(point)
                if point not in scanned_list:
                    x,y = point
                    for dx in [-1,0,1]:
                        for dy in [-1,0,1]:
                            if ((dx == 0) & (dy == 0)):
                                continue
                            if ((dx == 1) & (dy == 1)):
                                continue
                            if ((dx == 1) & (dy == -1)):
                                continue
                            if ((dx == -1) & (dy == 1)):
                                continue
                            if ((dx == -1) & (dy == -1)):
                                continue
                            if all([x+dx >= 0, x+dx < hmap.shape[1], y+dy >= 0, y+dy < hmap.shape[0]]):
                                if 9 > hmap[y+dy][x+dx] >= hmap[y][x]:
                                    print(f"Adding point ({x+dx},{y+dy}) with height {hmap[y+dy][x+dx]} to basin.")
                                    new_basin_points.append((x+dx,y+dy))
                    scanned_list.append(point)
            if basin_points == new_basin_points:
                print(f"Found low point ({X},{Y}) with basin size {len(list(set(new_basin_points)))}")
                return len(list(set(new_basin_points)))
            basin_points = new_basin_points
    return 0

basinmap = np.zeros(shape)
for y,row in enumerate(dl):
    for x,col in enumerate(row):
        basinmap[y][x] = basin_size(hmap,x,y)

answer = int(np.product(np.sort(basinmap.flatten())[::-1][:3]))

# %%
puzzle.answer_b = answer

# %%
