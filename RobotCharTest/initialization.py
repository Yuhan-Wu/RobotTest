import pygame
pygame.init()

from RobotCharTest.Robot import Robot
from RobotCharTest.Head import Head
from RobotCharTest.Body import Body
from RobotCharTest.RobotGun import RobotGun
from RobotCharTest.Cowboy import Cowboy
from RobotCharTest.Bullet import Bullet
from RobotCharTest.AmmoManager import AmmoManager

from RobotCharTest.Gun import Gun

win_width=1200
win_height=600

win_noise = 'WinSound.wav'
lose_noise = 'LoseSound.wav'

key=None

velocity=10

def detect_collision():
    winning=False
    failing=pygame.Rect.colliderect(bullet_from_robot.rect,cowboy.rect) or \
            pygame.Rect.colliderect(bullet.rect,cowboy.rect)

    if failing:
        cowboy.lose_sound()
        print("collide1")
        pygame.time.delay(1000)

    for bodypart in robot.bodyparts:
        if pygame.Rect.colliderect(bullet.rect,bodypart.rect):
            bullet.back()
            robot.sound()
            winning=robot.decrease_health(bodypart)
            print("collide")
            pygame.time.delay(1000)

    return winning,failing
    pass

def main():
    win=pygame.display.set_mode((win_width,win_height))
    win.blit(pygame.image.load("jellyfish.jpg"),(0,0))
    pygame.display.set_caption("Cowboy vs. Robot")

    global robot
    head=Head(path="robot_head_v1.png",position=(300,265))
    body=Body(path="robot_body_v1.png")
    robot_gun=RobotGun(path="robot_cannon_v1.png",position=(325,320))
    bodyparts=[]
    bodyparts.append(head)
    bodyparts.append(body)
    bodyparts.append(robot_gun)
    robot=Robot(bodyparts)
    robot.draw(win)

    global cowboy
    cowboy=Cowboy()
    cowboy.draw(win)

    #global bullet
    #bullet=Bullet()
    #bullet.draw(win)

    #DRAWING THE GUN
    global gun
    gun_image_path = "gun.png"
    gun_position = (300, 400)
    gun = Gun(gun_image_path, gun_position)

    #DRAWING THE BULLET
    global bullet
    bullet_image_path = "projectile.png"
    bullet_position = (300, 400)
    bullet = Bullet(bullet_image_path, bullet_position)

    global ammo_manager
    ammo_manager=AmmoManager()

    global bullet_from_robot
    bullet_from_robot=Bullet(position=(300,300))
    bullet_from_robot.draw(win)

    pygame.display.update()

    run=True

    isRotate = True
    angle = 0

    while run:
       pygame.time.delay(50)
       #for event in pygame.event.get():
       #    if event.type==pygame.QUIT:
       #         run=False

       for event in pygame.event.get():
            if ((event.type == pygame.KEYDOWN and event.key == pygame.K_q) or (event.type == pygame.QUIT)):
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                isRotate = False

       # change bullet position
       bullet.update_position(2*velocity)
       ammo_manager.update_reload(50)
       bullet_from_robot.update_position(-1*velocity)

       #ROTATION OF GUN AND BULLET SHOOTING
       if isRotate:
           angle += 10
           pass
       else:
           bullet.move(screen, angle, velocity)
           pass
       #bullet.draw(screen)
       gun.rotate(screen, angle)

       winning,failing=detect_collision()

       win.blit(pygame.image.load("jellyfish.jpg"), (0, 0))
       robot.draw(win)
       bullet.draw(win)
       bullet_from_robot.draw(win)
       cowboy.draw(win)
       if winning or failing:
           run=False
       pygame.display.update()

    if winning and not(failing):
        pygame.mixer.music.load(win_noise)
        pygame.mixer.music.play(loops=3, start=0)
        print("win")
        pass

    if failing:
        pygame.mixer.music.load(lose_noise)
        pygame.mixer.music.play(loops=3, start=0)
        print("fail")
        pass
    
    pygame.time.delay(1100)
    pass

main()