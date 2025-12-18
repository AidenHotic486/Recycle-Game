# create a game where various items spawn and move down. Player must click ONLY the paper bag. Speed and amount of items should increase over time

# Acomplish Today
#1. Spawn paper ag randomly within the list of scrap -- also fix mass spawning
#2. Force the scrap to move dow nthe screen at a fixed rate
#3. If the items get below the bottom of the screen .. (Do something)
import pgzrun
import time
import random

TITLE = "Recycle Paper Bags Game"
WIDTH, HEIGHT = 1000, 600
level = 1
scrapObjects = ["chipsimg", "paperimg", "bottleimg","batteryimg", "bagimg"]
#bag = "paperimg"
hasBag = False
currentObjects = []
spawnedActors = []
gameOver = False
animations = []



def randomOrder(objAmount):       # create the random order of 1 bag and 2 scrap items in a random order
    global scrapObjects, hasBag, currentObjects
    hasBag = False
    currentObjects.clear()
    for i in range(0, objAmount, 1):
        randNum = random.randint(1, 4)
        if randNum == 1:
            if hasBag:
                currentObjects.append(scrapObjects[0])
                pass
            else:
                hasBag = True
                currentObjects.append(scrapObjects[randNum])
        else:
            if i == objAmount - 1 and not hasBag:
                currentObjects.append(scrapObjects[1])
                hasBag = True
            else:
                currentObjects.append(scrapObjects[randNum])
    #print(currentObjects)

def spawnObject(object, posX, posY): # spawn a given image as a actor at a given pos
    global spawnedActors
    obj = Actor(object)
    obj.pos = (posX, posY)
    #obj.draw()
    spawnedActors.append(obj)
    return obj

def onGameOver():
    global gameOver
    gameOver = True
    print("Game Over")
    

def startRound():
    global spawnedActors, currentObjects
    spawnedActors.clear()
    randomOrder(level + 5)

    index = 0
    for objectName in currentObjects:
        spawnObject(objectName, 150 + index, 75)
        index += 75
    moveActors(spawnedActors)

def nextRound(): #Spawn items when a round starts
    global level
    
    print("Next Round Starting")
    
    level += 1
    startRound()


def on_mouse_down(pos):
    global spawnedActors
    if gameOver:
        return
    else:
        for char in spawnedActors:
            if char.collidepoint(pos):
                if "paperimg" in char.image:
                    print(char.image)
                    nextRound()
                else:
                    onGameOver()
        


def moveActors(chars):
    global animations
    animations.clear()
    for char in chars:
        #(char.pos)
        
        char.anchor = ("center", "bottom")
        animation = animate(char, duration = 5, on_finished = onGameOver, y = 600)
        animations.append(animation)


def draw():
    global spawnedActors, currentObjects

    screen.blit("bground", (0,0))
    
    index = 0
    for object in spawnedActors:
        object.draw()
        

def update():
    global spawnedActors, level, gameOver
    if not spawnedActors and not gameOver:
        startRound()

   

    
    


pgzrun.go()
