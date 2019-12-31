

with open("day19.txt") as file:
    data = file.read().splitlines()
starting = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"
"603 too high"


starting = "e"
data = """e => H
e => O
H => HO
H => OH
O => HH""".splitlines()

print(data)
replacements = []
for line in data:
    replacements.append(line.split(" => "))

print(replacements)
strings = []

#test = "testing stringey"
#print(test[:test.index("e")]+test[test.index("e")+1:])

def replace(string, repl, ind):
    temp = string[:ind]
    temp += repl[1]
    temp += string[ind+1:]

    return temp

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)



for i, j in replacements:
    for k in range(len(starting)):
        if starting[k:k+len(i)] == i:
            y = starting[:k] + j + starting[k+len(i):]
            if not y in strings:
                strings.append(y)

print(strings)
print(len(strings),"strings")
