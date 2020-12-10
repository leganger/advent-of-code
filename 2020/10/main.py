# Init
# %%
import numpy as np

with open("input.txt", "r") as infile:
    input_text = infile.read()[:-1]

input_list = input_text.split("\n")

nums = [int(x) for x in input_list]

# A
# %%
nums.append(0)
nums.sort()
nums

diffs = []
for i in range(len(nums)):
    if i<(len(nums)-1):
        diffs.append(nums[i+1]-nums[i])

diffs.append(3)

ones = [x for x in diffs if x==1]
threes = [x for x in diffs if x==3]

print(len(ones), len(threes))

len(ones) * len(threes)


# B
# %%
def connections_recursive(adapters, adapter, adapter_idx, pos_dict):
    possible = [x for x in adapters[(adapter_idx+1):(adapter_idx+4)] if ((x > adapter) & (x <= adapter+3))]

    if len(possible)==0:
        combinations = 1
    elif adapter_idx in pos_dict:
        combinations = pos_dict[adapter_idx]
    else:
        combinations = 0
        for pos in possible:
            pos_idx = adapters.index(pos)
            combinations += connections_recursive(adapters, pos, pos_idx, pos_dict)
        pos_dict[adapter_idx] = combinations
        print(adapter_idx, adapter, combinations)
    return combinations 


pos_dict = {}
connections_recursive(nums, 0, 0, pos_dict)
