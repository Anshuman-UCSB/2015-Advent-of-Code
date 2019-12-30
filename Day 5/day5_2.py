def repeatLetter(inp):
    last = "NULL"
    for ind, char in enumerate(inp):
        if ind>1:
            if char == inp[ind-2]:
                return True
    return False

def pairRepeat(inp):
    for i in range(len(inp)):
        if i>0:
            pair = inp[i-1:i+1]
            if pair in inp[i+1:]:
                return True
    return False

with open("day5.txt") as file:
    data = file.read().splitlines()

goodStrings = 0
for line in data:
    if pairRepeat(line) and repeatLetter(line):
        goodStrings+=1

print(goodStrings,"good strings.")
