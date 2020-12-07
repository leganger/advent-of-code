# Init
# %%
import numpy as np

with open("input.txt", "r") as infile:
    input_text = infile.read()[:-1]

input_list = input_text.split("\n")

# A
# %%
rules = [x.translate({ord(ch): None for ch in '0123456789 .'}).replace("bags","").replace("bag","").split("contain") for x in input_list]

color_dict = {}
for color in rules:
    contains_color = color[1].split(",")
    color_dict[color[0]] = contains_color 

contains_shinygold = {"shinygold"}

old_color_num = 0
for i in range(20):
    for color in color_dict:
        if any([x in contains_shinygold for x in color_dict[color]]):
            print(color, color_dict[color])
            contains_shinygold.add(color)
    
    print(contains_shinygold)
    old_color_num = len(contains_shinygold)        

len(contains_shinygold)-1


# B
# %%
rules = [x.replace(".","").replace(" ", "").replace("bags","").replace("bag","").split("contain") for x in input_list]

color_dict = {}
for color in rules:
    contains_color = [x[1:] for x in color[1].split(",")]
    contains_number = [x[0] for x in color[1].split(",")]

    color_dict[color[0]] = {}
    for ccolor, cnumber in zip(contains_color, contains_number):
        color_dict[color[0]][ccolor] = cnumber.replace("n","1")


def bag_recursive(bag, color_dict=color_dict):
    # base case
    if "oother" in color_dict[bag]:
        bag_count = 0
    else:
        bag_count = 0
        for sub_bag in color_dict[bag]:
            bag_count += int(color_dict[bag][sub_bag]) * (1 + bag_recursive(sub_bag))

    return bag_count


bag_recursive("shinygold")
