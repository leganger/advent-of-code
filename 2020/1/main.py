
#%%
import pandas as pd

input = pd.read_csv("input.txt", sep=" ", header=None)
input.columns=["entries"]
input = input.sort_values(by="entries", ascending=False)

for entry in input.entries:

    j = 1
    sum_entries = entry + input.entries.iloc[-j]

    while sum_entries < 2020:
        j += 1
        sum_entries = entry + input.entries.iloc[-j]

    if sum_entries == 2020:
        print(entry * input.entries.iloc[-j])
        break


# %%
result = None
for i, entry in enumerate(input.entries):
    if i == len(input.entries)-1:
        break

    for j in range(i+1, len(input.entries)):
        remainder = 2020 - entry - input.entries.iloc[j]
        if remainder > 0:
            for k in range(j+1, len(input.entries)):
                if input.entries.iloc[k] == remainder:
                    result = entry * input.entries.iloc[j] * input.entries.iloc[k]
                    print(result)
                    break
    if result: break



# %%
