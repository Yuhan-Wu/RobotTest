import pygame
pygame.init()

from RobotCharTest.Robot import Robot
from RobotCharTest.Head import Head
from RobotCharTest.Body import Body
from RobotCharTest.Bullet import Bullet

win_width=500
win_height=500

key=None

velocity=10

def detect_collision():

    for bodypart in robot.bodyparts:
        if pygame.Rect.colliderect(bullet.rect,bodypart.rect):
            bullet.visible=False
            winning=robot.decrease_health(bodypart)
        return winning

    pass

def main():
    win=pygame.display.set_mode((win_width,win_height))
    win.blit(pygame.image.load("jellyfish.jpg"),(0,0))
    pygame.display.set_caption("Cowboy vs. Robot")

    global winning
    global failing
    winning = False
    failing = False

    global robot
    head=Head()
    body=Body()
    bodyparts=[]
    bodyparts.append(head)
    bodyparts.append(body)
    robot=Robot(bodyparts)
    robot.draw(win)

    global bullet
    bullet=Bullet()
    bullet.draw(win)

    pygame.display.update()

    run=True
    while run:
       pygame.time.delay(50)
       for event in pygame.event.get():
           if event.type==pygame.QUIT:
                run=False
       bullet.update_position(velocity)
       win.blit(pygame.image.load("jellyfish.jpg"), (0, 0))
       robot.draw(win)
       bullet.draw(win)
       if winning:
           break
       pygame.display.update()

    if winning and not(failing):

        pass

    pass

main()