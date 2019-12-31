info = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".splitlines()


dict = {}
for line in info:
    split = line.split(": ")
    dict[split[0]] = int(split[1])

i = 0
for key, val in dict.items():
    print(i,key,":",val)
    i+=1

with open("day16.txt") as file:
    info = file.read().splitlines()

sues = []
def parse(line):
    split = line.split(" ")
    out = []
    out.append(int(split[1].strip(":")))
    try:
        ind = 2
        while True:
            out.append([split[ind][:-1], int(split[ind+1].strip(","))])
            ind+=2
    except:
        return out

for line in info:
    sues.append(parse(line))

def valid(sue):
    for i in range(1, len(sue)):
        key = sue[i][0]
        if key in ["cats", "trees"]:
            if dict[sue[i][0]] >= sue[i][1]:
                return False
        elif key in ["pomeranians", "goldfish"]:
            if dict[sue[i][0]] <= sue[i][1]:
                return False
        elif dict[sue[i][0]] != sue[i][1]:
            return False
    return True

for sue in sues:
    if valid(sue):
        print(sue)
