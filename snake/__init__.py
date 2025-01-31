from random import randint

def checkForObst(pos,list):
    for x in list:
        if x[0]==pos:
            return x[1]
    return pos

class game:
    def __init__(self, data):
        self.goes = 0
        self.running = True
        self.data = data
        self.playerData = {"turn":"human",
                           "CPU-1":1,
                           "CPU-2":1}
    def cpuGo(self, player):
        num = randint(1,6)
        self.playerData[player] += num
        landed = self.playerData[player]
        self.playerData[player] = checkForObst(self.playerData[player], self.data["snakes"])
        self.playerData[player] = checkForObst(self.playerData[player], self.data["ladders"])
       # print(f"{player} -- Roled {num}. Landed at {landed} Ended at {self.playerData[player]}")
        if self.playerData[player]>self.data["board"]:
            self.playerData[player] = self.data["board"]
        if self.playerData[player]==self.data["board"]:
            self.running = False
        self.goes += 1