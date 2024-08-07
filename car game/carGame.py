import pygame
import random
import math
import sys
pygame.init()   #This includes modules for handling the display, event management, font handling, sound, and more. Essentially, it prepares the Pygame library to be used.

# sound

pygame.mixer.music.load("Mix_audio.mp3")  # import music to play in background
pygame.mixer_music.play(-1)     # set music to play indefinitely

width=800
height=600
window=pygame.display.set_mode((800,600))  # pygame.display.set_mode use to define size of disply 600= width and 500 = height
pygame.display.set_caption("Run night") #  pygame.display.set_caption use to define the title of game/ display
logo=pygame.image.load('car1.jpg')
pygame.display.set_icon(logo)    #this will be the icon of game

# score
score=0   # use to count score
font=pygame.font.Font("freesansbold.ttf",32)  # font and its size
score_x=300
score_y=10

crash_x=20   # axis of message tos how afer car crash
crash_y=20

game_exit=False   #window will appear and nor exit
BackGroung=pygame.image.load('BGwM1.png')


maincar=pygame.image.load("cool1.jpg")   #add image of care to run
maincar_x=290
maincar_y=490
maincar_xchange=0
maincar_ychange=0

car1=pygame.image.load("cool22.jpg")   #add extra car to come from up
car1_x=290
car1_y=-100
car1_xchange=0
car1_ychange=3 # to run the opposite car

car2=pygame.image.load("cool333.jpg")   #add extra car to come from up
car2_x=290
car2_y=-100
car2_xchange=0
car2_ychange=3

car3=pygame.image.load("cool444.jpg")   #add extra car to come from up
car3_x=290
car3_y=-100
car3_xchange=0
car3_ychange=3

# show control keys

control_keys=pygame.image.load("keys.jpg")
control_keys_x=10
control_keys_y=10

control_space_key=pygame.image.load("space_key.jpg")
control_space_key_x=300
control_space_key_y=100

control_right_key=pygame.image.load("right key.jpg")
control_right_key_x=300
control_right_key_y=250

control_left_key=pygame.image.load("left_key.jpg")
control_left_key_x=300
control_left_key_y=400


def picture(x,y):
     window.blit(maincar,(x,y))

def picture_1(x,y):
     window.blit(car1,(x,y))

def picture_2(x,y):
     window.blit(car2,(x,y))

def picture_3(x,y):
     window.blit(car3,(x,y))

#collesion

def iscollesion(maincar_x,maincar_y,car_x,car_y):
     distnace=math.sqrt(math.pow(maincar_x-car_x,2)+math.pow(maincar_y-car_y,2))
     return distnace < 80

#score

def show_score(x,y):
     font_score = pygame.font.Font(None, 50)
     text_score=font_score.render("Score : "+str(score),True,(255,255,255))  # 255,255,255 = white color
     window.blit(text_score,(x,y))

def show_score_end(x,y):
     font_score = pygame.font.Font(None, 70)
     text_score=font_score.render("score : "+str(score),True,(0,0,0))  # 255,255,255 = white color
     window.blit(text_score,(x,y))

# crash window

def show_crash(x,y):
     font_crash = pygame.font.Font(None, 150)
     crash_text=font_crash.render("Car Crashed !!",True,(255,0,255))
     window.blit(crash_text,(x,y))
     pygame.display.flip()


clock = pygame.time.Clock()   # to control frame rate
paused = False

# Pause option

def pause():
    pygame.mixer_music.pause()
    global paused
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                    pygame.mixer_music.unpause()
                if event.key==pygame.K_q:
                    quit()
                if event.key == pygame.K_p:
                    reset_game()
                    return
                if event.key == pygame.K_c:
                    controls()
                    return
        window.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        text = font.render('Paused', True, (255, 0, 0))
        window.blit(text, (300,200))
        show_score(300,260)
        font2=pygame.font.Font(None,30)
        text2=font2.render("Press Space Button to resume the Game...",True,(255,255,255))
        window.blit(text2,(200,320))
        text3 = font2.render("Press p to play again", True, (255, 255, 255))
        window.blit(text3, (200, 360))
        text4=font2.render("Press c to check control flow",True,(255,255,255))
        window.blit(text4,(200,400))
        text5=font2.render("Press q to quit the game",True,(255,255,255))
        window.blit(text5,(200,440))

        pygame.display.flip()
        clock.tick(10)  

# TO check controls

def controls():
     checking=True
     while checking:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    checking=False
                    pause()
          window.fill((0,0,255))
          font2=pygame.font.Font(None,30)
          window.blit(control_keys,(control_keys_x,control_keys_y))
          text6=font2.render(".....KEYS..... ",True,(255,255,255))
          window.blit(text6,(50,220))
          window.blit(control_space_key,(control_space_key_x,control_space_key_y))
          text7=font2.render(" Space key to Pause/Resume the game",True,(255,255,255))
          window.blit(text7,(410,130))

          window.blit(control_right_key,(control_right_key_x,control_right_key_y))
          text8 = font2.render("Right key to move right ", True, (255, 255, 255))
          window.blit(text8, (410, 280))

          window.blit(control_left_key,(control_left_key_x,control_left_key_y))
          text9=font2.render("Left key to move Left",True,(255,255,255))
          window.blit(text9,(410,430))

          text10=font2.render("<----- Press Backspace to go back ....",True,(255,255,0))
          window.blit(text10,(250,570))

          pygame.display.flip()
          clock.tick(20)  

# to restart the game

def reset_game():
    global maincar_x, maincar_y, maincar_xchange, maincar_ychange, car1_x, car1_y, car1_xchange, car1_ychange
    global car2_x, car2_y, car2_xchange, car2_ychange, car3_x, car3_y, car3_xchange, car3_ychange, score, game_exit
    maincar_x = 290
    maincar_y = 490
    maincar_xchange = 0
    maincar_ychange = 0
    car1_x = 290
    car1_y = -100
    car1_xchange = 0
    car1_ychange = 3
    car2_x = 290
    car2_y = -100
    car2_xchange = 0
    car2_ychange = 3
    car3_x = 290
    car3_y = -100
    car3_xchange = 0
    car3_ychange = 3
    score = 0
    pygame.mixer_music.play(-1)
    game_exit = False

#main()/......
while not game_exit:
    window.blit(BackGroung,(0,0))
    for event in pygame.event.get():      #event is any operation like left move,right move ,quit window etc.. many operation are saved in pygame.event
            
            if event.type==pygame.QUIT:   #event.type means what instrucyion we gave to display that is present in pygame.event module
                game_exit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                      maincar_xchange=+2
                if event.key==pygame.K_LEFT:
                      maincar_xchange=-2
                if event.key == pygame.K_SPACE:
                    pause()
    maincar_x+=maincar_xchange
    car1_y+=car1_ychange
    car2_y+=car2_ychange
    car3_y+=car3_ychange

    if maincar_x<=170:
         maincar_x=170
    if maincar_x>=574:
         maincar_x=574

     # reverse car continue moving boundriess
    if car1_y>600:
          car1_y=-200
          car1_x=random.randint(170,574)
          score+=1
    if car2_y>600:
          car2_y=-500
          car2_x=random.randint(170,574)
          score+=1
    if car3_y>600:
          car3_y=-800
          car3_x=random.randint(170,574)
          score+=1
    collesion1=iscollesion(maincar_x,maincar_y,car1_x,car1_y)
    collesion2=iscollesion(maincar_x,maincar_y,car2_x,car2_y)
    collesion3=iscollesion(maincar_x,maincar_y,car3_x,car3_y)
            
     # reverse car continue moving boundriess
    picture(maincar_x,maincar_y)
    show_score(score_x,score_y)

    picture_1(car1_x,car1_y)
    picture_2(car2_x,car2_y)
    picture_3(car3_x,car3_y)

    if collesion1 or collesion2 or collesion3:
         pygame.mixer_music.stop()
         crash_sound=pygame.mixer.Sound('crash.wav')
         crash_sound.play()

         window.fill((255,255,0))  # fill screen with yellow color
         car1_ychange=0
         car2_ychange=0
         car3_ychange=0
         maincar_xchange=0
         maincar_ychange=0
         show_crash(crash_x,crash_y)
         show_score_end(300,200)
         font2 = pygame.font.Font(None, 50)
         text4 = font2.render("Press p to play again", True, (0, 0, 255))
         window.blit(text4, (250, 280))
         font2_1 = pygame.font.Font(None, 40)
         text4_1 = font2_1.render("Press (space) when game start to check controls", True, (255, 0, 0))
         window.blit(text4_1, (100, 350))
         pygame.display.flip()

         while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        reset_game()
                        break                                         
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
            else:
                continue
            break
    pygame.display.update()

pygame.quit()
quit()

