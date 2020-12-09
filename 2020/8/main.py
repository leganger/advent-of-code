# Init
# %%
import numpy as np

with open("input.txt", "r") as infile:
    input_text = infile.read()[:-1]

input_list = input_text.split("\n")

cmds = []
for x in input_list:
    x = x.split(" ")
    cmds.append([x[0], int(x[1]), 0])

# A
# %%
accumulator = 0

pos = 0

while True:
    cmd = cmds[pos]
    if cmd[2] > 0:
        break
    elif cmd[0] == "nop":
        cmds[pos][2] += 1
        pos += 1
    elif cmd[0] == "acc":
        accumulator += cmd[1]
        cmds[pos][2] += 1
        pos += 1
    elif cmd[0] == "jmp":
        cmds[pos][2] += 1
        pos += cmd[1]

accumulator


# B
# %%
cases = []
case = 0

for i, x in enumerate(input_list):
    x = x.split(" ")
    if x[0] in ["nop", "jmp"]:
        cmds = []
        for j, x in enumerate(input_list):
            x = x.split(" ")
            if i!=j:
                cmds.append([x[0], int(x[1]), 0, case])
            elif i==j:
                if x[0] == "nop":
                    cmds.append(["jmp", int(x[1]), 0, case])
                if x[0] == "jmp":
                    cmds.append(["nop", int(x[1]), 0, case])
        #print(cmds[:3])
        cases.append(cmds)
        case += 1

for cmds in cases:
    
    accumulator = 0
    pos = 0
    done = False

    while not done:
        if not pos<len(cmds):
            pass
        if pos<0:
            pass
        if pos == len(cmds):
            done = True
            break
        cmd = cmds[pos]
        if cmd[2] > 0:
            break
        elif cmd[0] == "nop":
            cmds[pos][2] += 1
            pos += 1
        elif cmd[0] == "acc":
            accumulator += cmd[1]
            cmds[pos][2] += 1
            pos += 1
        elif cmd[0] == "jmp":
            cmds[pos][2] += 1
            pos += cmd[1]
    
    if done:
        break

accumulator