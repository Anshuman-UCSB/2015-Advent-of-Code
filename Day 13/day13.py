from itertools import permutations

with open("day13.txt") as file:
    data = file.read().splitlines()

names = ["Me"]

def parse(line):
    split = line.split(" ")
    out = []
    out.append(split[0])
    out.append(int(split[3]))
    out.append(split[-1][:-1])

    if split[2] == "lose":
        out[1]*=-1

    if not out[0] in names:
        names.append(out[0])
    if not out[2] in names:
        names.append(out[2])

    return out

rules = []
for line in data:
    rules.append(parse(line))

def getDelta(name1, name2):
    delta = 0
    if name1== "Me" or name2 == "Me":
        return 0
    for rule in rules:
        if rule[0] == name1:
            if rule[2] == name2:
                delta += rule[1]
        if rule[0] == name2:
            if rule[2] == name1:
                delta += rule[1]
    return delta

def getHappiness(perm):
    sum = 0
    for i in range(len(perm)):
        sum += getDelta(perm[i],perm[(i+1)%len(perm)])
    return sum

arrangements = permutations(names)

hapi = []

for perm in arrangements:
    hapi.append(getHappiness(perm))

print(hapi)
print(max(hapi))
