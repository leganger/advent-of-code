# Init
# %%
import numpy as np
from aocd import get_data, submit

data = get_data(day=15,year=2020).splitlines()
data
# A
# %%
numbers = [int(x) for x in data[0].split(",")]

turn = 0

speak_list = []

for num in numbers:
    turn += 1
    speak_list.append(num)
    #print(turn, num)

while turn <= 2020:
    turn += 1
    last_num = speak_list[-1]
    if last_num in speak_list[:-1]:
        prev_spoke_turn = 1 + max([idx for idx, x in enumerate(speak_list[:-1]) if x==last_num])
        age = turn - 1 - prev_spoke_turn
        speak_list.append(age)
    else:
        age = 0
        speak_list.append(age)
    
    #print(turn, last_num, age)

answer = speak_list[-1]
answer


speak_list[-10:]
# %%
submit(answer)


# B

# %%
num_dict = {}
turn = 0
for num in numbers:
    turn += 1
    num_dict[num] = turn

next_num = 0
spoken = list(numbers)
turn += 1
while turn < 30000000:

    #spoken.append(next_num)

    if next_num in num_dict:
        age = turn - num_dict[next_num]
        num_dict[next_num] = turn
        next_num = age
    else:
        num_dict[next_num] = turn
        next_num = 0
        
    #print(turn, spoken)
    turn += 1

next_num

# %%
print(spoken)
print(speak_list)
# %%
submit(answer)
