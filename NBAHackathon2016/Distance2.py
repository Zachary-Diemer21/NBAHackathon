import numpy as np
import time
import csv
locset=[]
x=0
for i in range(12,51):
    
    if (x + 1) % 4 == 0:
        x=0
        continue
    locset.append(i)
    x += 1


#player location is an (x,y) tuple, ball location is a (x, y, z) or (x, y) tuple.
def distPoints(p1, p2):
    #print p1
    #print p2
    return (((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2))**.5

def distToBasket(point):
    basket1 = [5.25, 25]
    basket2 = [88.75, 25]
    dist1 = distPoints(basket1, point)
    dist2 = distPoints(basket2, point)
    if dist1 < dist2:
        return dist1
    return dist2

def closestPoint(node, nodes):
    closestDist = 99999
    closestPoint2 = 0
    i = 0
    for point in nodes:
        dist = distPoints(node, point)
        if closestDist > dist:
            closestDist == dist
            closestPoint2 = i
        i = i + 1
    return closestPoint2


    '''nodes = np.asarray(nodes)
    dist_2 = np.sum((nodes - node)**2, axis=1)
    return np.argmin(dist_2)'''

def splitPlayers(offensiveTeam, players):
    off = []
    defense = []
    for i in range(len(players)):
        if players[i] == offensiveTeam:
            off.append(i)
        else:
            defense.append(i)
    return (off, defense)


def findOffandDefPlayer(offTeam, ballPos, playersTeam, playersLoc, prevOffPlayer = None):
    #prevOff and prevDef are player Numbers (1 through 10)
    #playersLoc is [1ID, 1x, 1y, 2ID, 2x, 2y, etc]
    #returns false if no offensive player within 2 feet of ball
    #otherwise returns a tuple with offensive player, defensive player, off player position, def player position
    if ballPos[2] >= 10:
        return False #because the ball is clearly not posessed
    temp =splitPlayers(offTeam, playersTeam)
    off = temp[0]
    defense = temp[1]
    if prevOffPlayer is not None:
        if distPoints(ballPos, playersLoc[((prevOffPlayer * 3) - 2):(prevOffPlayer * 3)]) <= 5:
            offPlayer = prevOffPlayer
            offPlayerCoord = playersLoc[(offPlayer * 3) - 2: offPlayer * 3]

        else:
            points = []
            for player in off:
                player = player + 1
                points.append(playersLoc[(player * 3) - 2: player * 3])
            offPlayer = off[closestPoint(ballPos, points)]
            offPlayerCoord = playersLoc[(offPlayer * 3) - 2: offPlayer * 3]
            if distPoints(offPlayerCoord, ballPos) > 5:
                return False
    else:
        points = []
        for player in off:
            player = player + 1
            points.append(playersLoc[(player * 3) - 2: player * 3])
            #print points

        offPlayer = off[closestPoint(ballPos, points)] + 1
        offPlayerCoord = playersLoc[(offPlayer * 3) - 2: offPlayer * 3]
        if distPoints(offPlayerCoord, ballPos) > 5:
            return False
    points = []
    for player in defense:
        player = player + 1 #off by one error averted
        points.append(playersLoc[(player * 3) - 2: player * 3])
    defPlayer = defense[closestPoint(offPlayerCoord, points)] + 1
    defPlayerCoord = playersLoc[(defPlayer * 3) - 2: defPlayer * 3]

    return [offPlayer, defPlayer, offPlayerCoord, defPlayerCoord]

fraw=open('raw.csv', 'r')
rawreader=csv.reader(fraw)
raw=list(rawreader)

fposs=open('possposs.csv', 'r')
possreader=csv.reader(fposs)
poss=list(possreader)
playersLoc=[]
ball=[]
for i in range(10):
    players=[] #name, id, x, y
    for _ in range(10):
        p=[]
        c = 11
        d = 14
        p.append(raw[i][c:d+1])
        players.append(p)
        print(p)
        c += 4
        d += 4
    playersLoc.append(players)
    b=[]
    b.append([raw[i][8], raw[i][9]])
    ball.append(b)
    
    #find player closest to ball
    min = 9999
    name= None
    for each in players:
        dist_ball=((b[0]-each[2]) ** 2 + (b[1]-each[3]) ** 2 ) ** .5
        if dist_ball < min:
            min=dist_ball
            name=each[0]
    print(name)
# j=0
# offTeam= poss[j][5]
# for i in range(len(raw)):
    # if (poss[j][7] == raw[i][3] and poss[j][9]==raw[i][3]):
        # j += 1
        # offTeam= poss[j][5]
    # ballPos= (float(raw[i][8]), float(raw[i][9]), float(raw[i][10]))
    # playersTeam = raw[i][51:60]
    # playersLoc = []
    # for each in locset:
        # playersLoc.append(float(raw[i][each] if raw[i][each] != 'NULL' else 0))

    # result=findOffandDefPlayer(offTeam, ballPos, playersTeam, playersLoc, None)

    # print(str(result))


#test code below
'''
time1 = time.time()
for i in range(10):
    findOffandDefPlayer(1234567, (50, 50), [1234567, 1234568, 1234568, 1234567, 1234568, 1234567, 1234568, 1234567, 1234568, 1234567], [2, 50, 50, 3, 44, 51, 4, 55, 49, 5, 51, 50, 6, 33, 90, 7, 45, 51, 8, 50, 53, 9, 11,33, 10, 44, 45, 11, 46, 60], prevOffPlayer=None)
time2 = time.time()
print time2 - time1'''

#print splitPlayers(1, [1, 2, 2, 1, 1, 2, 2, 1])
#nodes = [(1, 1), (3, 3), (6, 6), (7, 8), (1, 0)]
#print nodes[closestPoint((2, 2), nodes)]