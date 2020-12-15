# Init
# %%
import numpy as np
from aocd import get_data, submit

data = get_data(day=13,year=2020).splitlines()
data

# A
# %%
target_time = int(data[0])
bus_times = [int(x) for x in data[1].replace("x,","").split(",")]

print(target_time)
print(bus_times)

earliest_times = []

for bus_time in bus_times:
    time = 0
    while time < target_time:
        time += bus_time
    earliest_times.append(time)

print(earliest_times)
bus_id = bus_times[earliest_times.index(min(earliest_times))]

print(bus_id)

answer = bus_id * (min(earliest_times)-target_time)
# %%
# submit(answer)


# B
# %% 
bus_ids = []
bus_offsets = []
for i, bus in enumerate(data[1].split(",")):
    if bus != "x":
        bus_ids.append(int(bus))
        bus_offsets.append(i)
               
bus_ids = np.array(bus_ids)
bus_offsets = np.array(bus_offsets)

bus_ids, bus_offsets
"""
multiplier = 1
done = False
while not done:
    print(multiplier)
    time = max(bus_ids) * multiplier - bus_offsets[np.argmax(bus_ids)]
    delta_offsets = (time + bus_offsets) % bus_id

    if np.all(delta_offsets == 0):
        answer = time
        done = True
    multiplier += 1

answer
"""
# %%
#submit(answer)
# %%
bus_ids

# %%
bus_offsets
# %%

period = 0:
    while 
