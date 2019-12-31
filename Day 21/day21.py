with open("day21.txt") as file:
    data = file.read().splitlines()

pHp = 100
pDmg = 0
pArm = 0
gold = 0

bHp = 104
bDmg = 8
bArm = 1

player = [pHp, pDmg, pArm]
boss = [bHp, bDmg, bArm]

def isPlayerWin(player):
    p = player.copy()
    b = boss.copy()

    while p[0] > 0:
        b[0] -= max(1, p[1]-b[2])
        if b[0] <= 0:
            return True
        p[0] -= max(1, b[1]-p[2])

        #print("Player hp:",p[0],", Boss hp:",b[0])
    return False

weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
armors = [[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5], [0, 0, 0]]
rings = [[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3], [0, 0, 0]]

maxGold = 0
build = []

for weapon in weapons:
    for armor in armors:
        for ring1 in rings:
            for ring2 in rings:
                if ring1 != ring2:
                    pTemp = player.copy()
                    perm = [weapon, armor, ring1, ring2]
                    gold = 0
                    for item in perm:
                        pTemp[1]+=item[1]
                        pTemp[2]+=item[2]
                        gold += item[0]
                    if not isPlayerWin(pTemp):
                        maxGold = max(gold, maxGold)
                        if gold == maxGold:
                            build = perm.copy()
                            print("Player lost with items",perm, "costing", gold)

print(maxGold)
