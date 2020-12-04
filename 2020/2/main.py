# %%
import pandas as pd

# %%
input = pd.read_csv("input.txt", sep=":", header=None)
input.columns=["policy","password"]
input.min = input.policy

# %%
input["min"] = input.policy.str.replace("-"," ").str.split(" ").map(lambda x: x[0])
input["max"] = input.policy.str.replace("-"," ").str.split(" ").map(lambda x: x[1])
input["letter"] = input.policy.str.replace("-"," ").str.split(" ").map(lambda x: x[2])
# %%
input["valid"] = False
for i in input.index:
    num_letters = sum([x == input.letter.iloc[i] for x in input.password.iloc[i]])

    if (num_letters >= int(input["min"].iloc[i])) & ((num_letters <= int(input["max"].iloc[i]))):
        input.valid.iloc[i] = True

sum(input.valid)

# %%
input.columns=["policy","password","first","second","letter","valid"]
input["valid"] = False

# %%
input["valid"] = False

from operator import itemgetter

for i, password in enumerate(input.password):
    relevant_letters = itemgetter(*[int(input["first"].iloc[i]),int(input["second"].iloc[i])])(password)
    matching_letters = [x == input.letter.iloc[i] for x in relevant_letters]
    if sum(matching_letters)==1:
        input["valid"].iloc[i] = True
    
    print(password, input["first"].iloc[i],input["second"].iloc[i], input["letter"].iloc[i], relevant_letters, matching_letters, input["valid"].iloc[i])

sum(input.valid)

# %%
