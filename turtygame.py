import turtle as trtl
import random as rand
import scoreManager as scMan
import playsound



#-----configuration-----

# configure & initalize window
screenH = 400
screenW = 500

wn = trtl.Screen()
img = "resources/qids.gif"
img2 = "resources/luigi.gif"
wn.setup(width=screenW, height=screenH)
wn.addshape(img)
wn.addshape(img2)

# configure turtle
chara = trtl.Turtle(shape=img)
chara.penup()
chara.speed(0)

# configure little item
littleItem = trtl.Turtle()
littleItem.shape("square")
littleItem.shapesize(0.4)
littleItem.penup()
littleItem.color("#0000FF")
littleItem.speed(0)
littleItem.goto(rand.randint(-220, 220), rand.randint(-175, 175))

# Setup score and fonts

fontSetup = ("Comic Sans MS", 20, "normal")

# Adds score counter
scoreWriter = trtl.Turtle()
scoreWriter.speed(0)
scoreWriter.penup()
scoreWriter.goto(-230,150)
scoreWriter.hideturtle()
scoreWriter.write("Score: " + str(scMan.scoreCounter), font=fontSetup)

# Add instructions text
instruct = trtl.Turtle()
instruct.speed(0)
instruct.penup()
instruct.goto(-165,-100)
instruct.hideturtle()
instruct.write("Use the arrow keys to move", font=fontSetup)

# Configure lois
lois = trtl.Turtle(shape=img2)
lois.hideturtle()
lois.penup()
lois.speed(0)

#-----variables-----

# Setup player coords and velocity
playerX = 0
playerY = 0
playerXvel = 0 
playerYvel = 0
playerVelocity = 2

#-----Game Functions-----

# Keyboard controls [i hate this compared to pygame]

def right():
    global playerXvel
    global playerYvel
    playerXvel = playerVelocity
    playerYvel = 0

def up():
    global playerYvel
    global playerXvel
    playerXvel = 0
    playerYvel = playerVelocity

def down():
    global playerYvel
    global playerXvel
    playerXvel = 0
    playerYvel = -playerVelocity

def left():
    global playerXvel
    global playerYvel
    playerXvel = -playerVelocity
    playerYvel = 0

def gameOver(gameOverTurt, turt, ItemTurt, scoreTurt):    
    scoreTurt.clear()
    scoreTurt.goto(0,50)
    scoreTurt.color("white")
    scoreTurt.write("Game over!", align="center", font=fontSetup)
    scoreTurt.goto(0,-100)
    scoreTurt.write("Score: " + str(scMan.scoreCounter) + "\n" + "Highscore: " + scMan.getHighscore("highscore.txt"), align="center", font=fontSetup)
    gameOverTurt.showturtle()
    turt.hideturtle()
    ItemTurt.hideturtle()

    playsound.playsound("scream.mp3")

def hideInstructions():
    instruct.clear()

# Character loop
def character(turt):
    global playerY
    global playerX
    while True:
        playerX += playerXvel
        playerY += playerYvel
        turt.goto(playerX, playerY)

        # Call item collision
        littleItemFunc()

        # Stop script if it hits the border
        if (turt.xcor() > 234) or (turt.xcor() < -234):
            gameOver(lois, chara, littleItem, scoreWriter)
            wn.bye()
            break
        elif (turt.ycor() > 184) or (turt.ycor() < -184):
            gameOver(lois, chara, littleItem, scoreWriter)
            wn.bye()
            break

# Item function
def littleItemFunc():
    global playerVelocity

    if littleItem.distance(chara) < 16:
        littleItem.goto(rand.randint(-220, 220), rand.randint(-175, 175))
        scMan.incrementScore()
        scoreWriter.clear()
        scoreWriter.write("Score: " + str(scMan.scoreCounter), font=fontSetup)
        playerVelocity += 2


#-----Game-----

# Key input
wn.onkeypress(hideInstructions)
wn.listen()
wn.onkey(right, "Right")
wn.onkey(up, "Up")
wn.onkey(down, "Down")
wn.onkey(left, "Left")

# Main Character Function
character(chara)
wn.mainloop()