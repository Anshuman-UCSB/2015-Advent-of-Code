start = "1321131112"

def iter(start):
    end = ""
    pos = 0
    while pos<len(start):
        count = 0
        char = start[pos]
        try:
            while start[pos] == char:
                count+=1
                pos+=1
        except:
            pass
        end+=str(count)+str(char)
    return end
print(start)
for i in range(50):
    start = iter(start)
    print(len(start))
