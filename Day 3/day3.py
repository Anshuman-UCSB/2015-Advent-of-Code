
with open("day3.txt") as file:
    data = file.read()


coords = []
loc = [0,0]
rloc = [0,0]

def addCoord():
    if not loc in coords:
        coords.append(loc.copy())
    if not rloc in coords:
        coords.append(rloc.copy())

addCoord()

for ind, instruction in enumerate(data):
    if ind%2==1:
        active = loc
    else:
        active = rloc
    if instruction == "^":
        active[1]+=1
    if instruction == ">":
        active[0]+=1
    if instruction == "v":
        active[1]-=1
    if instruction == "<":
        active[0]-=1
    addCoord()


print(len(coords))
