
alphabet = ['a','b','c','d','e','f','g','h',
        'i','j','k','l','m','n','o','p','q','r','s',
        't','u','v','w','x','y','z','a']

straights = []
bad = ["i","o","l"]

for i in range(len(alphabet)-3):
    straights.append(alphabet[i]+alphabet[i+1]+alphabet[i+2])

def hasStraight(inp):
    for straight in straights:
        if straight in inp:
            return True
    return False

def hasNoBad(inp):
    for b in bad:
        if b in inp:
            return False
    return True

def hasPairs(inp):
    count = 0
    for letter in alphabet[:-1]:
        if letter+letter in inp:
            count+=1

    return count>=2

def isValid(inp):
    return hasNoBad(inp) and hasStraight(inp) and hasPairs(inp)

def iterate(inp):

    inp = list(inp)
    out = ""
    ind = 1
    current = "a"
    try:
        while current == "a":
            inp[-ind] = alphabet[alphabet.index(inp[-ind])+1]
            current = inp[-ind]
            ind+=1
    except:
        "lmao"
    for char in inp:
        out+=char
    return out


input = "vzbxkghb"
pw = 0
while pw <= 1:
    input = iterate(input)
    valid = False
    while not valid:
        valid = isValid(input)
        if not valid:
            input = iterate(input)
        #print(input)
    pw+=1
    print(pw,":",input)
