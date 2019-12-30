with open("day7.txt") as file:
    data = file.read().splitlines()

dict = {}

debug = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i""".splitlines()

def parse(data):
    output = []
    for line in data:
        output.append(line.split(" "))
    for entry in output:
        entry.remove("->")
    return output

def act(instr):
    if len(instr)==2:
        try:
            dict[instr[1]]=int(instr[0])
        except:
            dict[instr[1]] = dict[instr[0]]
        "Set"
    params = []
    if "AND" in instr:
        try:
            params.append(dict[instr[0]])
        except:
            params.append(int(instr[0]))
        try:
            params.append(dict[instr[2]])
        except:
            params.append(int(instr[2]))
        dict[instr[-1]] = params[0] & params[1]
    if "OR" in instr:
        try:
            params.append(dict[instr[0]])
        except:
            params.append(int(instr[0]))
        try:
            params.append(dict[instr[2]])
        except:
            params.append(int(instr[2]))
        dict[instr[-1]] = params[0] | params[1]
    if "LSHIFT" in instr:
        try:
            params.append(dict[instr[0]])
        except:
            params.append(int(instr[0]))
        try:
            params.append(dict[instr[2]])
        except:
            params.append(int(instr[2]))
        dict[instr[-1]] = params[0] << params[1]
    if "RSHIFT" in instr:
        try:
            params.append(dict[instr[0]])
        except:
            params.append(int(instr[0]))
        try:
            params.append(dict[instr[2]])
        except:
            params.append(int(instr[2]))
        dict[instr[-1]] = params[0] >> params[1]
    if "NOT" in instr:
        try:
            params.append(dict[instr[1]])
        except:
            params.append(int(instr[1]))
        print("Not for",params)
        dict[instr[-1]] = ~ params[0] & 0xffff


parsed = parse(data)

for elem in parsed:
    dict[elem[-1]] = 0
for instr in parsed:
    act(instr)
print(dict)
print("a:",dict["a"])
