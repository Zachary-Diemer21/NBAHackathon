class players(object):
    playerDict = {}

    def __init__(self):
        playerDict = {}

    def playerO(self, playerID, change):
        if playerID in self.playerDict:
            self.playerDict[playerID][0] = self.playerDict[playerID][0] + change
            self.playerDict[playerID][2] = self.playerDict[playerID][2] + 1
        else:
            self.playerDict[playerID] = [change, 0, 1]
        return

    def playerD(self, playerID, change):
        if playerID in self.playerDict:
            self.playerDict[playerID][1] = self.playerDict[playerID][1] + change
            self.playerDict[playerID][2] = self.playerDict[playerID][2] + 1


        else:
            self.playerDict[playerID] = [0, change, 1]
        return
    def getPlayer(self, player):
        return self.playerDict[player]
