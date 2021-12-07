# Init
# %%
import numpy as np
from aocd.models import Puzzle

# %%
puzzle = Puzzle(year=2021, day=1)

# A
# %%
d = [int(s) for s in puzzle.input_data.splitlines()]
count = 0
m_prev = d[0]

for m in d:
    if m>m_prev:
        count += 1
    m_prev = m

print(count)
# %%
puzzle.answer_a = count


# B
# %%
d_sum = []
idx_max = len(d)
for idx in range(idx_max):
    if idx < 2:
        continue
    d_sum.append(d[idx-2]+d[idx-1]+d[idx])

count = 0
m_prev = d_sum[0]

for m in d_sum:
    if m>m_prev:
        count += 1
    m_prev = m


# %%
puzzle.answer_b = count