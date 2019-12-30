from itertools import permutations

with open("day9.txt") as file:
    data = file.read().splitlines()


"direction = [from, to, dist]"

def parse(line):
    "London to Dublin = 464"
    split = line.split()
    return [split[0],split[2],int(split[4])]

dirs = []
for line in data:
    dirs.append(parse(line))
locs = []
for dir in dirs:
    if not dir[0] in locs:
        locs.append(dir[0])
    if not dir[1] in locs:
        locs.append(dir[1])

def getDistance(place1, place2):
    places = [place1, place2]
    for direction in dirs:
        if direction[0] in places and direction[1] in places:
            return direction[2]
    return -1

def getPathDistance(path):
    totalDist = 0
    for i in range(len(path)-1):
        totalDist+=getDistance(path[i],path[i+1])
    return totalDist

paths = list(permutations(locs))
distances = []
for path in paths:
    distances.append(getPathDistance(path))
print(max(distances))
