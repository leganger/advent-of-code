# Init
# %%
import numpy as np
from aocd import get_data, submit

data = get_data(day=16,year=2020).splitlines()

rules = {}
for line in data[:20]:
    key = line.split(":")[0]
    range_a = line.replace(" ","").split(":")[1].split("or")[0].split("-")
    range_b = line.replace(" ","").split(":")[1].split("or")[1].split("-")
    rules[key] = {}
    rules[key]["a"] = (int(range_a[0]), int(range_a[1]))
    rules[key]["b"] = (int(range_b[0]), int(range_b[1]))

tickets = []
for line in data[25:]:
    tickets.append([int(x) for x in line.split(",")])

# A
# %%
valid_nums = set()
for rule in rules:
    valid_nums.update(range(rules[rule]["a"][0], rules[rule]["a"][1]+1))
    valid_nums.update(range(rules[rule]["b"][0], rules[rule]["b"][1]+1))

valid_nums

answer = 0
for ticket in tickets:
    for num in ticket:
        if num not in valid_nums:
            answer += num

answer
# %%
submit(answer)


# B
# %%
for ticket in tickets:
    for num in ticket:
        if num not in valid_nums:
            tickets.pop(tickets.index(ticket))
            break

fields = {}
for field_key in range(len(tickets[0])):
    fields[field_key] = {}
    fields[field_key]["values"] = []
    for ticket in tickets:
        fields[field_key]["values"].append(ticket[field_key])

for field in fields:
    fields[field]["allowed"] = []
    for rule in rules:
        allowed = set()
        allowed.update(range(rules[rule]["a"][0],rules[rule]["a"][1]+1))
        allowed.update(range(rules[rule]["b"][0],rules[rule]["b"][1]+1))
        if all(x in allowed for x in fields[field]["values"]):
            fields[field]["allowed"].append(rule)

popping = True
while popping:
    popping = False
    for field in fields:
        #print(field, fields[field]["allowed"])
        if len(fields[field]["allowed"])==1:
            for other_field in fields:
                if other_field != field:
                    if fields[field]["allowed"][0] in fields[other_field]["allowed"]:
                        popping = True
                        fields[other_field]["allowed"].pop(fields[other_field]["allowed"].index(fields[field]["allowed"][0]))

our_ticket = [int(x) for x in data[22].split(",")]

answer = 1
for field in fields:
    if fields[field]["allowed"][0][:3] == "dep":
        answer *= our_ticket[field]

answer
# %%
submit(answer)
