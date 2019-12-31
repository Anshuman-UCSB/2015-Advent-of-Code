with open("day15.txt") as file:
    data = file.read().splitlines()

def parse(line):
    split = line.split(" ")
    dat = []
    dat.append(split[0][:-1])
    dat.append(int(split[2][:-1]))
    dat.append(int(split[4][:-1]))
    dat.append(int(split[6][:-1]))
    dat.append(int(split[8][:-1]))
    dat.append(int(split[10]))

    return dat

ingredients = []

for line in data:
    ingredients.append(parse(line))
print(ingredients)

def validIngredients(inp):
    return sum(inp) == 100


def getScore(comp):
    product = 1
    for i in range(1,len(ingredients[0])-1):
        sum = 0
        for ing in range(len(comp)):
            sum+=comp[ing]*ingredients[ing][i]
        #print(sum)
        product *= sum
    return product if product > 0 else 0

maxScore = -1
for a in range(1,100):
    for b in range(1,101-a):
        for c in range(1,101-a-b):
            test = [a,b,c,100-a-b-c]
            if maxScore < getScore(test):
                maxScore = getScore(test)
                print(maxScore)
                print(test)
print(maxScore)

#40627200 too high
