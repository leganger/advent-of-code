# %%
import numpy as np
from aocd import get_data, submit

# %%
#seatmap = get_data(day=11,year=2020).splitlines()
with open("test_input.txt","r") as infile:
    seatmap = infile.read().splitlines()

seatmap = ["."+x+"." for x in seatmap]

seatmap = ["."*len(seatmap[0])]+seatmap+["."*len(seatmap[0])]

# %%
grid = np.zeros((len(seatmap),len(seatmap[0])))

done = False
while not done:
    old_grid=grid.copy()
    for i, row in enumerate(seatmap):
        if i==0:
            continue
        if i==len(seatmap):
            continue

        for j, char in enumerate(row):
            if j==0:
                continue
            if j==len(row):
                continue
            if char==".":
                continue
            if char=="L":
                occ_seats=old_grid[i-1,j-1]+old_grid[i-1,j]+old_grid[i-1,j+1]+old_grid[i,j-1]+old_grid[i,j+1]+old_grid[i+1,j-1]+old_grid[i+1,j]+old_grid[i+1,j+1]                
                print(occ_seats)
                    grid[i,j]=1
                if occ_seats >= 4:
                    if grid[i,j]==1:
                        grid[i,j]=0
    grid_compare = old_grid == grid
    if grid_compare.all():
        done = True

sum(grid.flatten())

# B
# %%
def see(grid,seatmap,x,y,x_step,y_step):
    x+=x_step
    y+=y_step
    while (0 <= x < grid.shape[0])&(0 <= y < grid.shape[1]):
        if seatmap[i][j]=="L":
            if grid[x,y]==1:
                return 1
            return 0
        elif seatmap[i][j]==".":
            x+=x_step
            y+=y_step
    return 0

grid = np.zeros((len(seatmap),len(seatmap[0])))

done = False
while not done:
    old_grid=grid.copy()
    for i, row in enumerate(seatmap):
        if i==0:
            continue
        if i==len(seatmap):
            continue

        for j, char in enumerate(row):
            if j==0:
                continue
            if j==len(row):
                continue
            if char==".":
                continue
            if char=="L":
                occ_seats=see(old_grid,i,j,-1,-1)+see(old_grid,i,j,-1,0)+see(old_grid,i,j,-1,+1)+see(old_grid,i,j,0,-1)+see(old_grid,i,j,0,+1)+see(old_grid,i,j,+1,-1)+see(old_grid,i,j,+1,0)+see(old_grid,i,j,+1,+1)
                if occ_seats == 0:
                    grid[i,j]=1
                if occ_seats >= 5:
                    if grid[i,j]==1:
                        grid[i,j]=0
        #print(grid[i,:])
    
    print(seatmap)
    print(old_grid)
    grid_compare = old_grid == grid
    if grid_compare.all():
        done = True

print(grid)

sum(grid.flatten())

# %%
print(grid)
# %%
print(seatmap)
# %%
