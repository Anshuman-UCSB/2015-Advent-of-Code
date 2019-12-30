with open("day1.txt") as file:
    data = file.read()

floor = 0
ind = 1
for char in data:
    if char == "(":
        floor+=1
    if char == ")":
        floor-=1
    if floor < 0:
        break
    ind+=1

print("Floor is:",floor)
print("Ind is:",ind)
