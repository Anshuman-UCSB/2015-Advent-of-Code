with open("day15.txt") as file:
    data = file.read().splitlines()

def parse(line):
    out = []
    split = line.split(" ")
    out.append(split[0][:-1])
    out.append(int(split[2][:-1]))
    out.append(int(split[4][:-1]))
    out.append(int(split[6][:-1]))
    out.append(int(split[8][:-1]))
    out.append(int(split[10]))
    return out

ingredients = []
for line in data:
    ingredients.append(parse(line))
    print(parse(line))

def score(counts):
    "counts = [25,25,25,25]... etc"
    if sum(counts) != 100:
        return -1
    prod = 1
    for attribute in range(1,len(ingredients[0])-1):
        total = 0
        for i in range(len(counts)):
            total += counts[i] * ingredients[i][attribute]
        prod *= max(total,0)
    cal = 0
    for i in range(len(counts)):
        cal += counts[i] * ingredients[i][-1]
    if cal == 500:
        return max(0,prod)
    return -1

maxScore = -1
frame, skip = 0,100
for a in range(1,100):
    for b in range(1,100-a):
        for c in range(1,100-a-b):
            val = score([a,b,c,100-a-b-c])
            maxScore = max(val, maxScore)
print("max:",maxScore)
