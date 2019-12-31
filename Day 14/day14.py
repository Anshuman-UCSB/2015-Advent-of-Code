
with open("day14.txt") as file:
    data = file.read().splitlines()

print(data)

def parse(line):
    "Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds."
    out = []
    split = line.split()
    out.append(int(split[3]))
    out.append(int(split[6]))
    out.append(int(split[-2]))
    return out

reindeers = []
for line in data:
    reindeers.append(parse(line))

for line in reindeers:
    print(line)

time = 2503

def calcDistance(deer, time):
    period = deer[1]+deer[2]
    dist = 0
    dist += int(time/period) * deer[0] * deer[1]
    time -= int(time/period)
    if time >= deer[1]:
        return dist + deer[0]*deer[1]
    else:
        return dist + time*deer[0]

distances = []
for deer in reindeers:
    distances.append(calcDistance(deer,2503))
print(distances)
print(max(distances))
