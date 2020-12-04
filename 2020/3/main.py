# Init
#%%
import pandas as pd
import numpy as np

map = pd.read_csv("input.txt", header=None)

# A
# %%
class Sled:
    def __init__(self, map, x=0 , y=0, x_step=3, y_step=1):
        self.map = map
        self.x = x
        self.y = y
        self.x_step = x_step
        self.y_step = y_step
        
        self.tree_count = 0

    def check_tree(self):
        map_x_length = len(self.map.iloc[0,0])
        map_x_position = self.x % map_x_length
        map_y_position = self.y

        map_value = self.map.iloc[map_y_position,0][map_x_position]
        if map_value == "#":
            self.tree_count += 1
    
    def move(self):
        self.x = self.x + self.x_step
        self.y = self.y + self.y_step

sled = Sled(map)

while sled.y < map.shape[0]:
    sled.check_tree()
    sled.move()

sled.tree_count


# B
#%%

tree_count_products = 1

for x_step, y_step in [(1,1),(3,1),(5,1),(7,1),(1,2)]:

    sled = Sled(map, x_step = x_step, y_step = y_step)

    while sled.y < map.shape[0]:
        sled.check_tree()
        sled.move()

    print(sled.tree_count)

    tree_count_products *= sled.tree_count
    #print(tree_count_products)

tree_count_products
