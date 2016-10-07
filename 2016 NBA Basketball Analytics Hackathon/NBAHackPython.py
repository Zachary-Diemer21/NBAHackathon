#Function to check which team has possession

class players(object):
    playerDict = {}

    def __init__(self):
        playerDict = {}

    def playerO(self, playerID, change):
        if playerID in self.playerDict:
            self.playerDict[playerID] = self.playerDict[playerID][0] + change
        else:
            self.playerDict[playerID] = [change, 0]
        return

    def playerD(self, playerID, change):
        if playerID in self.playerDict:
            self.playerDict[playerID] = self.playerDict[playerID][1] + change
        else:
            self.playerDict[playerID] = [0, change]
        return
    
    def getPlayer(self, player):
        return self.playerDict[player]

import numpy as np
import time

#player location is an (x,y) tuple, ball location is a (x, y, z) or (x, y) tuple.
def distPoints(p1, p2):
    #print p1
    #print p2
    return (((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2))**.5


def closestPoint(node, nodes):
    nodes = np.asarray(nodes)
    dist_2 = np.sum((nodes - node)**2, axis=1)
    return np.argmin(dist_2)

def splitPlayers(offensiveTeam, players):
    off = []
    defense = []
    for i in xrange(len(players)):
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
    temp = splitPlayers(offTeam, playersTeam)
    off = temp[0]
    defense = temp[1]
    if prevOffPlayer is not None:
        if distPoints(ballPos, playersLoc[((prevOffPlayer * 3) - 2):(prevOffPlayer * 3)]) <= 2:
            offPlayer = prevOffPlayer
            offPlayerCoord = playersLoc[(offPlayer * 3) - 2: offPlayer * 3]

        else:
            points = []
            for player in off:
                player = player + 1
                points.append(playersLoc[(player * 3) - 2: player * 3])
            offPlayer = off[closestPoint(ballPos, points)]
            offPlayerCoord = playersLoc[(offPlayer * 3) - 2: offPlayer * 3]
            if distPoints(offPlayerCoord, ballPos) > 2:
                return False
    else:
        points = []
        for player in off:
            player = player + 1
            points.append(playersLoc[(player * 3) - 2: player * 3])
            #print points

        offPlayer = off[closestPoint(ballPos, points)] + 1
        offPlayerCoord = playersLoc[(offPlayer * 3) - 2: offPlayer * 3]
        if distPoints(offPlayerCoord, ballPos) > 2:
            return False
    points = []
    for player in defense:
        player = player + 1 #off by one error averted
        points.append(playersLoc[(player * 3) - 2: player * 3])
    defPlayer = defense[closestPoint(offPlayerCoord, points)] + 1
    defPlayerCoord = playersLoc[(defPlayer * 3) - 2: defPlayer * 3]

    return offPlayer, defPlayer, offPlayerCoord, defPlayerCoord

#should read in the file once, and then continually reference the file 
def checkPossession(pos_Team, gameClock, gameClock_end): 
	#Need to know the Offensive and Defensive Team IDS everytime it ends a possession, it has to check the offensive team id
	if(gameClock == gameClock_end):
		#Check CSV for the first row and input the data into gameClock_end()
		updateData, however you do this #aka update pos_team, gameClock, gameClock_end 
		return new values of pos_Team, gameClock, gameClock_end






		#Find which is the offensive team, and return that id 

		#defTeam = offTeam 
		#offTeam = temp 
	#return offTeam, defTeam 

	#This is the game and this is the time who had the ball last 



#test code below


'''
time1 = time.time()
for i in range(10):
    findOffandDefPlayer(1234567, (50, 50), [1234567, 1234568, 1234568, 1234567, 1234568, 1234567, 1234568, 1234567, 1234568, 1234567], [2, 50, 50, 3, 44, 51, 4, 55, 49, 5, 51, 50, 6, 33, 90, 7, 45, 51, 8, 50, 53, 9, 11,33, 10, 44, 45, 11, 46, 60], prevOffPlayer=None)
time2 = time.time()
print time2 - time1'''
