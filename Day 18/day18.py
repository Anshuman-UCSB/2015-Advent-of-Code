size = 6
temp = [0 for i in range(size+2)]
grid = [temp.copy() for i in range(size+2)]

with open("day18.txt") as file:
    data = file.read().splitlines()
    grid.clear()
    for line in data:
        grid.append([0])
        for val in line:
            if val == ".":
                grid[-1].append(0)
            else:
                grid[-1].append(1)
        grid[-1].append(0)
    grid.insert(0, [0 for i in range(len(grid[1]))])
    grid.append([0 for i in range(len(grid[1]))])



def printGrid():
    for row in grid:
        for val in row:
            if val == 0:
                print(".",end="")
            else:
                print("#",end="")
        print()

def getNeighbors(x,y):
    total = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i != 0 or j !=0:
                print(x,y, i,j)
                if grid[y+j][x+i] in [-1,1]:
                    total += grid[y+j][x+i]
    return total

def update():
    for x in range(1,len(grid)-1):
        for y in range(1,len(grid[0])-1):
            if grid[y][x] == 1:
                if not getNeighbors(x,y) in [2,3]:
                    grid[y][x] = -1
            elif grid[y][x] == 0:
                if getNeighbors(x, y) == 3:
                    grid[y][x] = 2
    for x in range(1,len(grid)-1):
        for y in range(1,len(grid[0])-1):
            if grid[y][x]<0:
                grid[y][x] = 0
            elif grid[y][x]>1:
                grid[y][x] = 1

printGrid()
while True:
    input()
    update()
    printGrid()
