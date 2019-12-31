with open("day18.txt") as file:
    data = file.read().splitlines()

grid = []
for line in data:
    grid.append([])
    for val in line:
        if val == ".":
            grid[-1].append(0)
        else:
            grid[-1].append(1)

temp = [0 for i in range(len(grid))]
tgrid = [temp.copy() for i in range(len(grid))]


def printGrid():
    for line in grid:
        for val in line:
            if val == 1:
                print("#",end="")
            else:
                print(".",end="")
        print()

def getNeighbors(x,y):
    total = 0
    for i in range(-1,2):
        for j in range(-1,2):
            try:
                if i!=0 or j!=0:
                    if y+j != -1 and x+i != -1:
                        total+=grid[y+j][x+i]
            except:
                pass
    return total

def update():
    grid[0][0] = 1
    grid[0][-1] = 1
    grid[-1][0] = 1
    grid[-1][-1] = 1
    for x in range(len(grid)):
        for y in range(len(grid)):
            tgrid[y][x] = 0
            if grid[y][x] == 1:
                if getNeighbors(x, y) in [2,3]:
                    tgrid[y][x] = 1
                else:
                    tgrid[y][x] = 0
            elif grid[y][x] == 0:
                if getNeighbors(x, y) == 3:
                    tgrid[y][x] = 1
                else:
                    tgrid[y][x] = 0
    tgrid[0][0] = 1
    tgrid[-1][0] = 1
    tgrid[0][-1] = 1
    tgrid[-1][-1] = 1
    for x in range(len(grid)):
        for y in range(len(grid)):
            grid[y][x] = tgrid[y][x]

printGrid()
count = 0
while count!=100:
    count+=1
    print(count)
    update()
    #printGrid()

total = 0
for row in grid:
    total+=sum(row)
print(total)
