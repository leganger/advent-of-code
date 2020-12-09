# Init
# %%
import numpy as np

with open("input.txt", "r") as infile:
    input_text = infile.read()[:-1]

input_list = input_text.split("\n")

nums = [int(x) for x in input_list]

# A
# %%
def possibilities(nums):
    pos = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j:
                pos.append(nums[i]+nums[j])
    return pos

for i, num in enumerate(nums[25:]):
    end = 25 + i
    if num not in possibilities(nums[i:end]):
        break

num

# B
# %%
key = num
done = False

for i, num in enumerate(nums):
    j = i
    numsum = num
    while numsum < key:
        j += 1
        numsum += nums[j]
        if numsum == key:
            answer = min(nums[i:j+1])+max(nums[i:j+1])
            done = True
            break
    if done:
        break

answer


# %%
