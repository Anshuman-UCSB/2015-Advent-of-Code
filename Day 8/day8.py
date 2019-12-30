with open("day8.txt") as file:
    data = file.read().splitlines()
total = 0
needsEsc = ["\\","\"","\'","\\x"]
for line in data:
    sum = 2
    for val in line:
        if val in needsEsc:
            sum+=1
    total+=sum

print(total)

#1448 too low
