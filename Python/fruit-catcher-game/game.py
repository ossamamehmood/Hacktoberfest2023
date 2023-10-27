import pygame
import random
import math
pygame.init()
pygame.display.set_caption('Fruit Catcher - Subham Roy')
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 20)
background_img = pygame.image.load("assets/garden.jpg")
background_img = pygame.transform.scale(background_img, (screen.get_width(), screen.get_height()))
player_img=pygame.transform.scale(pygame.image.load("assets/basket.png"),(100,100))
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
apple=pygame.transform.scale(pygame.image.load("assets/apple.png"),(50,50))
banana=pygame.transform.scale(pygame.image.load("assets/banana.png"),(50,50))
mango=pygame.transform.scale(pygame.image.load("assets/mango.png"),(50,50))
orange=pygame.transform.scale(pygame.image.load("assets/orange.png"),(50,50))
pineapple=pygame.transform.scale(pygame.image.load("assets/pineapple.png"),(50,50))
strawberry=pygame.transform.scale(pygame.image.load("assets/strawberry.png"),(50,50))
objectiveArr=[apple,banana,mango,orange,pineapple,strawberry]
coordinates=[-1,0,1]
objectives=[]
objectiveSpeed=80
playerSpeed=500
score=0
wave=0
numberOfFruitGenratedPerWave=20
def generateObjective():
    t=[]
    for i in range(numberOfFruitGenratedPerWave):
        vx,vy=coordinates[random.randint(0,2)],coordinates[random.randint(0,2)]
        while vx==0 and vy==0:
            vx,vy=coordinates[random.randint(0,2)],coordinates[random.randint(0,2)]
        t.append([objectiveArr[random.randint(0, 5)],pygame.Vector2(random.randint(10,1270),random.randint(10,710)),vx,vy])
    return t
def hasCollided(obj1,x,y):
    if math.sqrt(((obj1.x-x)**2)+((obj1.y-y)**2))<=100:
        return True 
    else:
        return False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background_img, (0, 0)) 
    if len(objectives)==0:
        wave+=1
        objectives=generateObjective()
    for o in objectives:
        screen.blit(o[0],o[1])
    screen.blit(player_img,player_pos)
    screen.blit(font.render("Score :"+str(score)+"  Wave:"+str(wave)+"  Score Per Wave:"+str(round(score/wave,2)), True, green, blue),pygame.Vector2(10,10))
    screen.blit(font.render("W,S,A,D - Move Basket   SPACE - Collect Fruit   ESC - Quit Game", True, green, blue),pygame.Vector2(10,690))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running=False
    if keys[pygame.K_w]:
        player_pos.y -= playerSpeed * dt
    if keys[pygame.K_s]:
        player_pos.y += playerSpeed * dt
    if keys[pygame.K_a]:
        player_pos.x -= playerSpeed * dt
    if keys[pygame.K_d]:
        player_pos.x += playerSpeed * dt
    if keys[pygame.K_SPACE]:
        temp2=[]
        for o in objectives:
            if hasCollided(player_pos,o[1].x,o[1].y):
                score+=50
            else:
                temp2.append(o)
        objectives=temp2
    temp=[]
    for o in objectives:
        o[1].x+=o[2]*dt*objectiveSpeed
        o[1].y+=o[3]*dt*objectiveSpeed
        if o[1].x>=0 and o[1].x<=1280 and o[1].y>=0 and o[1].y<=720:
            temp.append(o)
    objectives=temp
    pygame.display.flip()
    dt = clock.tick(60) / 1000 
pygame.quit()