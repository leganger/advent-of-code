# Init
# %%
import numpy as np

with open("input.txt", "r") as infile:
    input_text = infile.read()

input_list = input_text.split("\n")

for i, element in enumerate(input_list):
    if len(element)!=10:
        input_list.pop(i)

# A
# %%
seats = np.zeros((len(input_list),3))

# %%
for i, text in enumerate(input_list):

    lower_row = 0
    upper_row = 127

    for char in text[:7]:

        if char == "F":
            upper_row = lower_row + int((upper_row-lower_row)/2)

        if char == "B":
            lower_row = lower_row + int((upper_row-lower_row)/2)+1
        
        print(char, lower_row, upper_row)
    
    seats[i,0] = lower_row

    lower_column = 0
    upper_column = 7

    for char in text[7:]:

        if char == "L":
            upper_column = lower_column + int((upper_column-lower_column)/2)

        if char == "R":
            lower_column = lower_column + int((upper_column-lower_column)/2)+1

        print(char, lower_column, upper_column)

    seats[i,1] = lower_column

    seats[i,2] = seats[i,0]*8 + seats[i,1]

    if lower_row==0:
        break

print(np.min(seats[:,2]))
print(np.max(seats[:,2]))

# %%


# B
all_ids_set = set(range(np.min(seats.astype("int")[:,2]), np.max(seats.astype("int")[:,2])+1))
taken_ids_set = set(seats.astype("int")[:,2])

all_ids_set - taken_ids_set