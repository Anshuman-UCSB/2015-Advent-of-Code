grid = [[0 for y in range(1000)] for x in range(1000)]


def getSum():
    global grid
    sum = 0
    for row in grid:
        for val in row:
            sum+=val
    return sum

def turnOn(p1, p2):
    global grid
    x1 = p1[0]
    x2 = p2[0]

    y1 = p1[1]
    y2 = p2[1]


    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            grid[y][x]+=1

def turnOff(p1, p2):
    global grid
    x1 = p1[0]
    x2 = p2[0]

    y1 = p1[1]
    y2 = p2[1]

    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if grid[y][x]>=1:
                grid[y][x]-=1


def toggle(p1, p2):
    global grid
    x1 = p1[0]
    x2 = p2[0]

    y1 = p1[1]
    y2 = p2[1]

    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            grid[y][x]+=2

def parse(inp):
    for line in inp:
        if "on" in line:
            split = line.split(" ")

            p1 = split[2].split(",")
            p1[0] = int(p1[0])
            p1[1] = int(p1[1])

            p2 = split[4].split(",")
            p2[0] = int(p2[0])
            p2[1] = int(p2[1])

            turnOn(p1,p2)
        if "off" in line:
            split = line.split(" ")

            p1 = split[2].split(",")
            p1[0] = int(p1[0])
            p1[1] = int(p1[1])

            p2 = split[4].split(",")
            p2[0] = int(p2[0])
            p2[1] = int(p2[1])

            turnOff(p1,p2)
        if "toggle" in line:
            split = line.split(" ")

            p1 = split[1].split(",")
            p1[0] = int(p1[0])
            p1[1] = int(p1[1])

            p2 = split[3].split(",")
            p2[0] = int(p2[0])
            p2[1] = int(p2[1])

            toggle(p1,p2)

with open("day6.txt") as file:
    parse(file.read().splitlines())

print(getSum())
