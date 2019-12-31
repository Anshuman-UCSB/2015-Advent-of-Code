reindeers = []
dists = {}
points = {}

class deer:
    def __init__(self, line):
        "Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds."
        split = line.split()
        self.time = 0
        self.distance = 0

        self.name = split[0]
        self.speed = int(split[3])
        self.duration = int(split[6])
        self.rest = int(split[-2])

        self.period = self.rest+self.duration
        dists[self.name] = self.distance
        points[self.name] = 0

    def __str__(self):
        return "{} currently at {}km.".format(self.name, self.distance)

    def iterate(self):
        if self.time%self.period < self.duration:
            "Currently in motion"
            self.distance += self.speed
        self.time+=1
        dists[self.name] = self.distance


with open("day14.txt") as file:
    data = file.read().splitlines()

for line in data:
    reindeers.append(deer(line))


while reindeers[0].time!=2503:
    #print("    Time",reindeers[0].time+1)
    for deer in reindeers:
        deer.iterate()
        #print(deer)

    names = []
    max = -1
    for key, val in dists.items():
        if val > max:
            max = val
            names = [key]
        elif val == max:
            names.append(key)
    for name in names:
        points[name]+=1


for key, val in points.items():
    print(key,":",val)
