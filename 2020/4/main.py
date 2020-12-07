# Init
#%%
import numpy as np

with open("input.txt", "r") as infile:
    batch_text = infile.read()

passports = batch_text.split("\n\n")

pdict = {}
id = 0
for passport in passports:
    pdict[id] = {}
    elements = passport.replace("\n"," ").split(" ")
    for element in elements:
        #print(element)
        if ":" in element:
            key = element.split(":")[0]
            value = element.split(":")[1]
            pdict[id][key] = value
    id += 1

# A
# %%
validcount = 0
mandatory = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional = ["cid"]

for id in pdict:
    valid = True
    for key in mandatory:
        if key not in pdict[id].keys():
            valid = False
    if valid:
        validcount += 1

validcount

# B
# %%
def val_num(val, digits, min, max):
    if len(str(val)) != digits:
        return False
    if int(val) < min:
        return False
    if int(val) > max:
        return False
    return True

def val_byr(val):
    return val_num(val, 4, 1920, 2002)

def val_iyr(val):
    return val_num(val, 4, 2010, 2020)

def val_eyr(val):
    return val_num(val, 4, 2020, 2030)

def val_hgt(val):
    if val[-2:] == "cm":
        return val_num(val[:-2], 3, 150, 193)
    if val[-2:] == "in":
        return val_num(val[:-2], 2, 59, 76)
    return False

def val_hcl(val):
    if val[0] == "#":
        if len(val[1:])==6:
            valid = True
            for char in val[1:]:
                if char not in "0123456789abcdef":
                    valid = False
            return valid
    return False

def val_ecl(val):
    return val in ["amb","blu","brn","gry","grn","hzl","oth"]

def val_pid(val):
    if len(str(val)) != 9:
        return False
    return True


validcount = 0
for id in pdict:
    valid = True
    for key in mandatory:
        if key not in pdict[id].keys():
            valid = False
    if valid:        
        checklist = []
        checklist.append(val_byr(pdict[id]["byr"]))
        checklist.append(val_iyr(pdict[id]["iyr"]))
        checklist.append(val_eyr(pdict[id]["eyr"]))
        checklist.append(val_hgt(pdict[id]["hgt"]))
        checklist.append(val_hcl(pdict[id]["hcl"]))
        checklist.append(val_ecl(pdict[id]["ecl"]))
        checklist.append(val_pid(pdict[id]["pid"]))

        print(
            [pdict[id]["byr"],
            pdict[id]["iyr"],
            pdict[id]["eyr"],
            pdict[id]["hgt"],
            pdict[id]["hcl"],
            pdict[id]["ecl"],
            pdict[id]["pid"]]
            )

        print(checklist)

        if False not in checklist:
            validcount += 1

validcount

# %%

