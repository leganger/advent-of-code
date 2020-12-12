# %%
import numpy as np
from aocd import get_data, submit

# %%
data = get_data(day=12,year=2020).splitlines()

# %%
data

# A
# %%
class Ferry():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = "E"
        self.dir_to_deg = {"E":0,"N":90,"W":180, "S":270}
        self.deg_to_dir = {0:"E",90:"N",180:"W", 270:"S"}

    def turn(self, command):
        if command[0] == "L":
            sign = 1
        if command[0] == "R":
            sign = -1
        new_deg = self.dir_to_deg[self.direction] + sign*int(command[1:])
        while new_deg >= 360:
            new_deg -= 360
        while new_deg < 0:
            new_deg += 360
        self.direction = self.deg_to_dir[new_deg]
    
    def move(self, command):
        if command[0]=="F":
            if self.direction == "E":
                self.x += int(command[1:])
            if self.direction == "N":
                self.y += int(command[1:])
            if self.direction == "W":
                self.x -= int(command[1:])
            if self.direction == "S":
                self.y -= int(command[1:])
        if command[0] == "E":
            self.x += int(command[1:])
        if command[0] == "N":
            self.y += int(command[1:])
        if command[0] == "W":
            self.x -= int(command[1:])
        if command[0] == "S":
            self.y -= int(command[1:])
        
    def parse_cmd(self, command):
        if command[0] in ["L","R"]:
            self.turn(command)
        if command[0] in ["E","N","W","S","F"]:
            self.move(command)

ferry = Ferry()

for command in data:
    ferry.parse_cmd(command)
    print(command[0], int(command[1:]), ferry.x, ferry.y, ferry.direction)

# %%
submit(abs(ferry.x)+abs(ferry.y))


# B
# %%
class Ferry_B():
    def __init__(self):
        self.ferry_x = 0
        self.ferry_y = 0
        self.x = 10
        self.y = 1
        self.dir_to_deg = {"E":0,"N":90,"W":180, "S":270}
        self.deg_to_dir = {0:"E",90:"N",180:"W", 270:"S"}

    def turn_90(self, direction):
        if direction == "L":
            new_x = -self.y 
            new_y = self.x
        if direction == "R":
            new_x = self.y
            new_y = -self.x
        self.x = new_x
        self.y = new_y

    def turn(self, command):
        turn_degs = int(command[1:])
        while turn_degs >= 90:
            self.turn_90(command[0])
            turn_degs -= 90
    
    def move(self, command):
        if command[0]=="F":
            self.ferry_x += self.x*int(command[1:])
            self.ferry_y += self.y*int(command[1:])
        if command[0] == "E":
            self.x += int(command[1:])
        if command[0] == "N":
            self.y += int(command[1:])
        if command[0] == "W":
            self.x -= int(command[1:])
        if command[0] == "S":
            self.y -= int(command[1:])
        
    def parse_cmd(self, command):
        if command[0] in ["L","R"]:
            self.turn(command)
        if command[0] in ["E","N","W","S","F"]:
            self.move(command)

ferry = Ferry_B()

for command in data:
    ferry.parse_cmd(command)
    print(command[0], int(command[1:]), ferry.x, ferry.y, ferry.ferry_x, ferry.ferry_y)

abs(ferry.ferry_x)+abs(ferry.ferry_y)

# %%
submit(abs(ferry.ferry_x)+abs(ferry.ferry_y))
