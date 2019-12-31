import json

with open("day12.txt") as file:
    data = file.read()

unwound = []
dicts = {}

dat = json.loads(data)
for elem, key in dat.items():
    print (elem, type(key))

listType = type([])
dictType = type({})


def unwindList(list):
    for val in list:
        if type(val) == listType:
            unwindList(val)
        elif type(val) == dictType:
            unwindDict(val)
        else:
            unwound.append(val)


def unwindDict(dict):
    for val in dict.values():
        if val == "red":
            return
    for key, val in dict.items():
        if type(val) == listType:
            unwindList(val)
        elif type(val) == dictType:
            unwindDict(val)
        else:
            unwound.append(val)

unwindDict(dat)
print(unwound)

def getSum():
    sum = 0
    for val in unwound:
        try:
            sum+=int(val)
        except:
            pass
    return sum

print(getSum())
