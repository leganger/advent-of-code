# Init
# %%
import numpy as np

with open("input.txt", "r") as infile:
    input_text = infile.read()[:-1]

input_list = input_text.split("\n\n")

# A
# %%
yes_counts = [len(list(set(x.replace("\n","")))) for x in input_list]

sum(yes_counts)# %%

# B
# %%
all_yes_count = 0
for group in input_list:
    count = 0
    group_list = group.split("\n")
    for char in group_list[0]:
        in_all = True
        for answers in group_list[1:]:
            if char not in answers:
                in_all = False
        if in_all:
            count += 1
    print(group_list, count)
    all_yes_count += count

all_yes_count
