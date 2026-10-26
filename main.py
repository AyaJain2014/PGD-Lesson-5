import pgzrun, random

WIDTH = 400
HEIGHT = 400
TITLE = "Bee Game"

bee = Actor("bee")
bee.pos = (100,100)
flower = Actor("flower")
flower.pos = (200,200)

score = 0
gameover = False

def draw():
    screen.blit("grass",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score :"+str(score), color = "black", topleft = (10,10))
    if gameover:
        screen.fill("blue")
        screen.draw.text("Your score was :"+str(score), color = "black", midtop = (WIDTH/2,10))

def move_flower():
    flower.x = random.randint(50,350)
    flower.y = random.randint(50,350)

def update():
    global score
    if keyboard.left:
        bee.x = bee.x-2
    if keyboard.right:
        bee.x = bee.x+2
    if keyboard.up:
        bee.y = bee.y-2
    if keyboard.down:
        bee.y = bee.y+2
    if bee.colliderect(flower):
        score += 10
        move_flower()

def timer():
    global gameover
    gameover = True


clock.schedule(timer, 60.0)

pgzrun.go()