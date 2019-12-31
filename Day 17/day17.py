with open("day17.txt") as file:
    data = file.read().splitlines()

cups = []
for line in data:
    cups.append(int(line))

cups.sort()
cups.reverse()
print(len(cups),"cups.")
print(cups)

max = 2**len(cups)-1
print(max)
eggnog = 150
combos = []

minCups = len(cups)+1
minCount = 0

for i in range(max):
    total = 0
    inp = bin(i)[2:]
    size = len(str(inp))
    counts = [int(k) for k in "0"*(len(cups)-size)+inp]
    if sum(counts)>minCups:
        continue
    for i in range(len(counts)):
        total += counts[i]*cups[i]
        if total>eggnog:
            break
    if total == eggnog:
        minCount+=1
        if sum(counts)<minCups:
            minCups = sum(counts)
            minCount = 1
        #print(counts)

print(minCups)
print(minCount)
