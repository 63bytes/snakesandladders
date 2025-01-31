import snake
import json

goes = []
avg = 0

def runGame():
    SNL = snake.game(json.load(open("board.json","r")))
    while SNL.running:
        SNL.cpuGo("CPU-1")
    goes.append(SNL.goes)

for x in range(10000):
    print(f"{x}/10000")
    runGame()

for x in goes:
    avg += x
print(avg/len(goes))