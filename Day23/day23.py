from Processor import Processor

registers = {'a':0, 'b':0}
pointer = 0

data = """inc a
jio a, +2
tpl a
inc a""".splitlines()

with open("day23.txt") as file:
    data = file.read().splitlines()

def parse(line):
    split = line.split(" ")
    if "inc" in line:
        return [split[0],split[1]]
    if "hlf" in line:
        return [split[0],split[1]]
    if "tpl" in line:
        return [split[0],split[1]]
    if "jmp" in line:
        offset = int(split[1])
        return [split[0],offset]

    offset = int(split[2])
    return [split[0], split[1][:-1], offset]

instructions = []
for line in data:
    instructions.append(parse(line))


prc = Processor(instructions)
prc.regs['a'] = 1

while not prc.finished:
    prc.process()
    print(prc.regs)
