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
    failing=pygame.Rect.colliderect(bullet_from_robot.rect,cowboy.rect)
    if failing:
        print("collide1")

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
    # head=Head()
    body=Body()
    bodyparts=[]
    # bodyparts.append(head)
    bodyparts.append(body)
    robot=Robot(bodyparts)
    robot.draw(win)

    global cowboy
    cowboy=Cowboy()
    cowboy.draw(win)

    global bullet
    bullet=Bullet()
    bullet.draw(win)

    global bullet_from_robot
    bullet_from_robot=Bullet(position=(300,300))
    bullet_from_robot.draw(win)

    pygame.display.update()

    run=True
    while run:
       pygame.time.delay(50)
       for event in pygame.event.get():
           if event.type==pygame.QUIT:
                run=False

       # change bullet position
       bullet.update_position(velocity)
       bullet_from_robot.update_position(-2*velocity)

       detect_collision()

       win.blit(pygame.image.load("jellyfish.jpg"), (0, 0))
       robot.draw(win)
       bullet.draw(win)
       bullet_from_robot.draw(win)
       cowboy.draw(win)
       if winning or failing:
           break
       pygame.display.update()

    if winning and not(failing):
        print("win")
        pass

    if failing:
        print("fail")
        pass

    pass

main()