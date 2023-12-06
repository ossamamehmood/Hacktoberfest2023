import pygame
import random
import math
import cv2
import mediapipe as mp

pygame.init()
pygame.display.set_caption('Fruit Catcher - Subham Roy')
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

green = (0, 255, 0)
blue = (0, 0, 128)

font = pygame.font.Font('freesansbold.ttf', 20)
background_img = pygame.image.load("assets/garden.jpg")
background_img = pygame.transform.scale(background_img, (screen.get_width(), screen.get_height()))
player_img=pygame.transform.scale(pygame.image.load("assets/basket.png"),(100,100))
apple=pygame.transform.scale(pygame.image.load("assets/apple.png"),(50,50))
banana=pygame.transform.scale(pygame.image.load("assets/banana.png"),(50,50))
mango=pygame.transform.scale(pygame.image.load("assets/mango.png"),(50,50))
orange=pygame.transform.scale(pygame.image.load("assets/orange.png"),(50,50))
pineapple=pygame.transform.scale(pygame.image.load("assets/pineapple.png"),(50,50))
strawberry=pygame.transform.scale(pygame.image.load("assets/strawberry.png"),(50,50))

dt=0
objectiveArr=[apple,banana,mango,orange,pineapple,strawberry]
coordinates=[-1,0,1]
objectives=[]
objectiveSpeed=50
score=0
wave=0
numberOfFruitGenratedPerWave=15

def is_palm_closed(hand_landmarks):
    thumb = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    index_finger = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_TIP]
    pinky_finger = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_TIP]

    thumb_to_index_dist = abs(thumb.x - index_finger.x) + abs(thumb.y - index_finger.y)
    thumb_to_middle_dist = abs(thumb.x - middle_finger.x) + abs(thumb.y - middle_finger.y)
    thumb_to_ring_dist = abs(thumb.x - ring_finger.x) + abs(thumb.y - ring_finger.y)
    thumb_to_pinky_dist = abs(thumb.x - pinky_finger.x) + abs(thumb.y - pinky_finger.y)

    threshold = 0.1
    if (
        thumb_to_index_dist < threshold and
        thumb_to_middle_dist < threshold and
        thumb_to_ring_dist < threshold and
        thumb_to_pinky_dist < threshold
    ):
        return True
    else:
        return False
    
def player_position(x,y):
    return [int(x*1280),int(y*720)]

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
    
mp_hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    image = cv2.flip(image, 1)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = mp_hands.process(image_rgb)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False      
        
    is_closed=False    
    player_pos = pygame.Vector2(0,0)
    screen.blit(background_img, (0, 0)) 
    if len(objectives)==0:
        wave+=1
        objectives=generateObjective()
    for o in objectives:
        screen.blit(o[0],o[1])
        
    screen.blit(font.render("Score :"+str(score)+"  Wave:"+str(wave)+"  Score Per Wave:"+str(round(score/wave,2)), True, green, blue),pygame.Vector2(10,10))
    screen.blit(font.render("Move Hands - Move Basket   Close Hands - Collect Fruit   ESC - Quit Game", True, green, blue),pygame.Vector2(10,690)) 
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            
            is_closed = is_palm_closed(hand_landmarks)
            x = min(lm.x for lm in hand_landmarks.landmark)
            y = min(lm.y for lm in hand_landmarks.landmark)
            w = max(lm.x for lm in hand_landmarks.landmark) - x
            h = max(lm.y for lm in hand_landmarks.landmark) - y
            
            [px,py]=player_position(x,y)
            player_pos = pygame.Vector2(px,py)
            screen.blit(player_img,player_pos)
    
    if is_closed:
        temp2=[]
        for o in objectives:
            if hasCollided(player_pos,o[1].x,o[1].y):
                score+=50
            else:
                temp2.append(o)
        objectives=temp2 
     
    keys = pygame.key.get_pressed()   
    if keys[pygame.K_ESCAPE]:
         break  
    
    temp=[]          
    for o in objectives:
        o[1].x+=o[2]*dt*objectiveSpeed
        o[1].y+=o[3]*dt*objectiveSpeed
        if o[1].x>=0 and o[1].x<=1280 and o[1].y>=0 and o[1].y<=720:
            temp.append(o)
    objectives=temp      
    pygame.display.flip()
    dt = clock.tick(30) / 1000 
    
cap.release()
cv2.destroyAllWindows()
pygame.quit()