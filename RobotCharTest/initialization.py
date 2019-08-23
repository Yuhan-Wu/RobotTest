import pygame
pygame.init()

from RobotCharTest.Robot import Robot
from RobotCharTest.Head import Head
from RobotCharTest.Body import Body
from RobotCharTest.BodyPart import Body_Part
from RobotCharTest.Bullet import Bullet
from RobotCharTest.AmmoManager import AmmoManager

win_width=500
win_height=500

win_noise = 'WinSound.wav'
lose_noise = 'LoseSound.wav'

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
    head=Body_Part(1, "../robot_head_v1.png", (303, 263))
    body=Body_Part(1, "../robot_body_v1.png", (300, 300))
    gun = Body_Part(0, "../robot_cannon_v1.png", (333, 313))
    bodyparts=[]
    bodyparts.append(head)
    bodyparts.append(body)
    bodyparts.append(gun)
    robot=Robot(bodyparts)
    robot.draw(win)

    global bullet
    bullet=Bullet()
    bullet.draw(win)

    global ammo_manager
    ammo_manager=AmmoManager()

    pygame.display.update()

    run=True
    while run:
       pygame.time.delay(50)
       for event in pygame.event.get():
           if event.type==pygame.QUIT:
                run=False
       bullet.update_position(velocity)
       gun.rotate(5)
       ammo_manager.update_reload(50)
       win.blit(pygame.image.load("jellyfish.jpg"), (0, 0))
       robot.draw(win)
       bullet.draw(win)
       gun.draw(win)
       if winning:
           pygame.mixer.music.load(win_noise)
           pygame.mixer.music.play(loops = 3, start = 0)
           break
       pygame.display.update()

    if winning and not(failing):

        pass

    pass

main()