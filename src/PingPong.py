print('PP started')
#Import
import pygame
import random
import time
from pygame.locals import *
#Screen and Setup

fpsClock=pygame.time.Clock()

def display4(msg,x,y,color,size):
    pygame.font.init()
    fontobj=pygame.font.SysFont("freesjans",size)
    msgobj=fontobj.render(msg,False,color)
    util.screen.blit(msgobj,(x,y))

class util:
    #Color
    screen=pygame.display.set_mode((1000,600))
    BLACK =(0,0,0)
    WHITE =(255,255,255)
    RED   =(255,0,0)
    PINK  =(255,0,255)
    YELLOW=(255,255,0)
    GREEN =(0,255,0)
    BLUE  =(0,0,255)
    TEAL  =(0,255,255)
    clist=[RED,GREEN,BLUE,TEAL,PINK,YELLOW,BLACK,WHITE]
    xchange=1
    ychange=1

    #Variables
    ballstartx=400
    ballstarty=300
    radiusstart=10
    
    lch=0
    rch=0

    wait=0

    Lpaddlepoints=0
    Rpaddlepoints=0

class ball:
    #Attributes
    def __init__(self, ballx, bally, color, radius):
        self.ballx = ballx
        self.bally = bally
        self.color= color
        self.radius = radius

    def draw(self):
        pygame.draw.circle(util.screen,self.color,(self.ballx,self.bally),self.radius)
              
    def move(self):
        self.ballx=self.ballx+util.xchange
        self.bally=self.bally+util.ychange

class paddle:
    def __init__(self, paddlex, paddley, color, width, height, speed):
        self.paddlex=paddlex
        self.paddley=paddley
        self.color=color
        self.width=width
        self.height=height
        self.speed=1

    def draw(self):
        pygame.draw.rect(util.screen,self.color,(self.paddlex,self.paddley,self.width,self.height))

    def move(self, direction):
        if (direction == "U1" or direction == "U2") and self.paddley > 5:
            self.paddley = self .paddley-1
        if (direction == "D1" or direction == "D2")  and self.paddley < 495:
            self.paddley = self .paddley+1

pygame.display.set_caption("Ping Pong")
util.screen.fill((255,255,255))

obj_ball = ball(util.ballstartx,util.ballstarty,util.BLUE,util.radiusstart)
obj_left_paddle = paddle(5,395,util.BLACK,5,100,1)
obj_right_paddle = paddle(990,395,util.BLACK,5,100,1)
ldown=0
rdown=0
lup=0
rup=0
Game = True
while Game:
    fpsClock.tick(1000)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            Game = False
        if event.type == KEYDOWN:
            if event.key==K_DOWN:
                rdown=1
                   
            if event.key==K_UP:
                rup=1
                    
            if event.key==K_s:
                ldown=1

            if event.key==K_w:
                lup=1

        if event.type==KEYUP:
            if event.key==K_DOWN:
                rdown=0
                   
            if event.key==K_UP:
                rup=0
                    
            if event.key==K_s:
                ldown=0

            if event.key==K_w:
                lup=0
    
    if rdown == 1:
        obj_right_paddle.move("D1")
    if rup == 1:
        obj_right_paddle.move("U1")
    if ldown == 1:
        obj_left_paddle.move("D1")
    if lup == 1:
        obj_left_paddle.move("U1")
    if Game:
        util.screen.fill((255,255,255))
    obj_ball.draw()
    obj_right_paddle.draw()
    obj_left_paddle.draw()
    obj_ball.ballx = obj_ball.ballx + util.xchange
    obj_ball.bally = obj_ball.bally + util.ychange

    if obj_ball.ballx == obj_right_paddle.paddlex and obj_right_paddle.paddley<obj_ball.bally<obj_right_paddle.paddley+100:
        util.xchange=-util.xchange

    if obj_ball.ballx == obj_left_paddle.paddlex and obj_left_paddle.paddley<obj_ball.bally<obj_left_paddle.paddley+100:
        util.xchange=-util.xchange

    if obj_ball.bally == 600 or obj_ball.bally == 0:
        util.ychange=-util.ychange

    if obj_ball.ballx == 1000:
        util.Lpaddlepoints=util.Lpaddlepoints+1
        obj_ball.ballx = 500
        obj_ball.bally = 400
        obj_ball.draw()
        time.sleep(1)

    if obj_ball.ballx == 0:
        util.Rpaddlepoints=util.Rpaddlepoints+1
        obj_ball.ballx = 500
        obj_ball.bally = 400
        obj_ball.draw()
        time.sleep(1)

    if util.Rpaddlepoints==3:
        display4('THE RIGHT PLAYER WINS',0,20,util.GREEN,50)
        time.sleep(1)
        util.Rpaddlepoints=0
    
    if util.Lpaddlepoints==3:
        display4('THE LEFT PLAYER WINS',0,20,util.GREEN,50)
        time.sleep(1)
        util.Lpaddlepoints=0
    if Game:
        pygame.display.update()
    if util.wait==0:
        time.sleep(3)
        util.wait=1
        
            
    












    
















    



