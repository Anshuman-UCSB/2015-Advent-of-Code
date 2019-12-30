with open("day2.txt") as file:
  data = file.read().splitlines()

ribbon = 0
paper = 0
for size in data:
    dim = size.split("x")
    l = int(dim[0])
    w = int(dim[1])
    h = int(dim[2])
    SA = [l*w, w*h, h*l]
    paper += 2*(SA[0]+SA[1]+SA[2]) + min(SA)

    ribbon += l*w*h
    sides = [l,w,h]
    sides.remove(max(sides))
    ribbon += 2*(sides[0]+sides[1])

print("Paper needed:",paper)
print("Ribbon needed:",ribbon)
