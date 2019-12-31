with open("day12.txt") as file:
    data = file.read()

print(data)

sum = 0
ind = 0
while ind < len(data):
    canBeNum = False
    try:
        int(data[ind])
        canBeNum = True
    except:
        canBeNum = "-" == data[ind]
    size = 1
    if canBeNum:
        try:
            while True:
                size+=1
                int(data[ind:ind+size])
        except:
            "finished size"
            size-=1

        sum+=(int(data[ind:ind+size]))
    ind+=size
print(sum)
