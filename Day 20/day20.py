from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def fact(n):
    prod = 1
    for i in range(1,n+1):
        prod*=i
    return prod

def getPresents(houseNum):
    val = 0
    for i in range(1,houseNum+1):
        if houseNum%i == 0:
            val += i
    return val*10



def presentsFactors(houseNum):
    return 10 * sum(factors(houseNum))

inp = 29000000
def part2():
    houses = [11 for i in range(int(inp/11))]
    print("initialized houses with len",len(houses))
    for i in range(2,int(inp/11)):
        #input()
        for j in range(i,50*i+1,i):
            #print(j)
            try:
                houses[j] += 11*i
            except:
                pass
        if houses[i] >= inp:
            print(i,":",houses[i])
    print("starting part 2")

    for i, val in enumerate(houses):
        if val >= inp:
            print(i,":",val)


part2()
exit()

house = 0
presents = -1
while presents < inp:
    house+=1
    presents = presentsFactors2(house)
    if house%10000 == 0:
        print("house",house,":",presents)

print("house",house,":",presents)
