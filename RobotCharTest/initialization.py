import pygame
import math
pygame.init()

from RobotCharTest.Robot import Robot
from RobotCharTest.Head import Head
from RobotCharTest.Body import Body
from RobotCharTest.Gun import Gun
from RobotCharTest.Cowboy import Cowboy
from RobotCharTest.RobotGun import RobotGun
from RobotCharTest.Bullet import Bullet
from RobotCharTest.AmmoManager import AmmoManager

win_width=1200
win_height=600

win_noise = 'WinSound.wav'
lose_noise = 'LoseSound.wav'

clock = pygame.time.Clock()
key=None


# CONFIG PARAMETER
bullet_speed=40
bullet_position = (220, win_height-160)
cowboy_gun_rot_speed = 20
robot_gun_rot_speed = -0.5

def detect_collision():
    winning=False
    failing= pygame.Rect.colliderect(robot_bullet.rect, cowboy.rect) or \
             pygame.Rect.colliderect(cowboy_bullet[ammo_manager.get_ammo_index()].rect, cowboy.rect)

    if failing:
        cowboy.lose_sound()
        print("collide1")
        #pygame.time.delay(1000)

    for bodypart in robot.bodyparts:
        for b in cowboy_bullet:
            if pygame.Rect.colliderect(b.rect, bodypart.rect):
                b.reset()
                robot.sound()
                winning = robot.decrease_health(bodypart)
                print("collide")
                if winning:
                    break
                # pygame.time.delay(1000)

    return winning,failing
    pass

def main():
    clock.tick(60)
    win=pygame.display.set_mode((win_width,win_height))
    pygame.display.set_caption("Cowboy vs. Robot")
    bg1=pygame.image.load("SpaceBackground(Rapid).png").convert_alpha()
    bg2=pygame.image.load("alien_land_v1.png").convert_alpha()

    global robot
    head=Head(path="robot_head_v1.png",position=(win_width-300,win_height-200))
    body=Body(path="robot_body_v1.png",position=(win_width-300,win_height-160))
    robot_gun=RobotGun(path="robot_cannon_v1.png",position=(win_width-270,win_height-160))
    bodyparts=[]
    bodyparts.append(head)
    bodyparts.append(body)
    bodyparts.append(robot_gun)
    robot=Robot(bodyparts)
    robot.draw(win)

    global cowboy
    cowboy=Cowboy("cowboy_v1.png", (100, win_height-200))
    cowboy.draw(win)

    global cowboy_gun
    gun_image_path = "gun_v1.png"
    cowboy_gun_position = (210, win_height-160)
    cowboy_gun = Gun(gun_image_path, cowboy_gun_position)
    cowboy_gun.draw(win)

    global ammo_manager
    ammo_manager=AmmoManager()

    global cowboy_bullet
    bullet_image_path = "robot_bullet_v1.png"
    cowboy_bullet=[]
    counter = ammo_manager.ammo_capacity
    while counter > 0:
        b = Bullet(bullet_image_path, bullet_position)
        cowboy_bullet.append(b)
        counter -= 1

    global robot_bullet
    robot_bullet=Bullet(bullet_image_path, position=(win_width-270,win_height-120))
    robot_bullet.draw(win)

    pygame.display.update()

    angle = 0

    run=True
    while run:
       #pygame.time.delay(50)
       for event in pygame.event.get():
           if ((event.type == pygame.KEYDOWN and event.key == pygame.K_q) or \
                   (event.type == pygame.QUIT)):
               run = False
           if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
               if ammo_manager.try_shoot():
                print(ammo_manager.ammo)
                cowboy_bullet[ammo_manager.get_ammo_index()].shoot(angle)

       ammo_manager.update_reload(50)

       win.blit(bg1, (0, 0))
       win.blit(bg2, (0, 0))

       robot.draw(win)
       cowboy.draw(win)

       if not robot_gun.rotate(robot_gun_rot_speed, 320):
           robot_bullet.velocity=(-1, 0) * bullet_speed
           robot_bullet.update_position(bullet_speed)
           pygame.mixer.music.load("RobotLaserSound.wav")
           pygame.mixer.music.play(loops=1, start=0)
           robot_bullet.draw(win)


       for b in cowboy_bullet:
           b.update_position(bullet_speed)
           if b.visibility:
            b.draw(win)

       angle += cowboy_gun_rot_speed
       cowboy_gun.rotate(win, angle)

       winning,failing=detect_collision()

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
    
    #pygame.time.delay(100)
    pass

main()