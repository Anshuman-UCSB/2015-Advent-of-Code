vowels = ['a','e','i','o','u']
bad = ['ab','cd','pq','xy']

def hasBad(inp):
    for val in bad:
        if val in inp:
            return True
    return False

def hasDup(inp):
    last = "NULL"
    for val in inp:
        if val == last:
            return True
        last = val
    return False

def hasVowels(inp):
    vowelCount = 0
    for char in inp:
        if char in vowels:
            vowelCount+=1
        if vowelCount >= 3:
            return True
    return False

def isNice(str):
    return hasVowels(str) and hasDup(str) and not hasBad(str)

with open("day5.txt") as file:
    data = file.read().splitlines()

goodStrings = 0
for line in data:
    if isNice(line):
        goodStrings+=1

print(goodStrings,"nice strings.")
