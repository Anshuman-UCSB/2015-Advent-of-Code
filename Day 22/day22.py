player = [50, 0, 500, 0]

def charLost(char):
    if char[0] <= 0:
        return True
    if char[2] <= 53:
        return True

boss = [104, 8]

def bossLost(boss):
    return boss[0]<=0

timers = [0, 0, 0, 0, 0]

spells = ["Magic Missile", "Drain", "Shield", "Poison", "Recharge"]

def bossAtk(char):
    #print("Boss atk char for",max(boss[1]-char[1],1))
    char[0] -= max(boss[1]-char[1],1)

def playerAtk(player, spell, timers):
    #print("Player atk timers",timers)

    if timers[spell] > 0:
        return False
    #print("Player cast",spells[spell])
    if spell == 0:
        player[2] -= 53
        player[3] += 53
        boss[0] -= 4
    elif spell == 1:
        player[2] -= 73
        player[3] += 73
        boss[0] -= 2
        player[0] += 2
    elif spell == 2:
        player[2] -= 113
        player[3] += 113
        timers[spell] = 6
    elif spell == 3:
        player[2] -= 173
        player[3] += 173
        timers[spell] = 6
    elif spell == 4:
        player[2] -= 229
        player[3] += 229
        timers[spell] = 5

def updateTimers(player, timers):
    for i, val in enumerate(timers):
        if val>0:
            if i == 2:
                player[1] = 7
            if i == 3:
                boss[0] -= 3
            if i == 4:
                player[2] += 101
            timers[i] -= 1
    #print("at here, timer is",timers)

moveset = [0,1,2,3,4]

def buildList(n):
    list = []
    while n>4:
        list.append(n%5)
        n = int(n/5)
    list.append(n)

    return list

def moves():
    ind = 0
    while True:
        yield buildList(ind)
        ind+=1

frame = [0,1000]
def isPlayerWin(moves):
    #print()
    if frame[0]%frame[1] == 0:
        print(" > Attemping with moves",moves)
    frame[0]+=1
    timers = [0, 0, 0, 0, 0]
    boss = [104, 8]
    player = [50, 0, 500, 0]

    ind = 0
    while True:
        #print("timers:",timers)
        if charLost(player):
            #print("Player died/OOM")
            return False
        updateTimers(player, timers)
        try:
            if playerAtk(player, moves[ind], timers) == False:
                #print("Duplicate effect")
                #print(ind)
                return False
        except:
            #print("Out of moves")
            return False
        ind+=1
        if bossLost(boss):
            print("Boss died")
            print("Boss:",boss)
            print("Player:",player)
            return True
        updateTimers(player, timers)
        bossAtk(player)
        #print("    Player:",player)
        #print("    Boss:",boss)

for move in moves():
    if isPlayerWin(move):
        input("Won")
    #input()
