#-----scoreManager for turty game  :-)-----

# Define global scoreCounter variable
scoreCounter = 0

def incrementScore():
    global scoreCounter
    scoreCounter+= 1

def decrementScore():
    global scoreCounter
    scoreCounter-= 1

def resetScore():
    global scoreCounter
    scoreCounter = 0

def getHighscore(fileName):
    global scoreCounter
    highScoreFile = open(fileName, "r")

    for line in highScoreFile:
        index = 0
        highScoreStr = ""

        while (line[index] != "\n"):
            highScoreStr = highScoreStr + line[index]
            index+=1
    
    highScoreFile.close()

    if scoreCounter > int(highScoreStr):
        updateHighscore(fileName)
        return highScoreStr
    else:
        return highScoreStr


def updateHighscore(fileName):
    global scoreCounter
    file = open(fileName, "w")

    file.write(str(scoreCounter) + "\n")