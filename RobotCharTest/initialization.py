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
from RobotCharTest.Drone import Drone


win_width=1200
win_height=600
win=pygame.display.set_mode((win_width,win_height))

win_noise = 'WinSound.wav'
lose_noise = 'LoseSound.wav'

clock = pygame.time.Clock()
key=None
global will_reset
will_reset = False

# CONFIG PARAMETER
bullet_speed=5
bullet_position = (220, win_height-160)
cowboy_gun_rot_speed = 1
robot_gun_rot_speed = 0
drone_speed = 1
global canDamage
canDamage = 0

def detect_collision():
    global canDamage
    winning=False

    droneCollision = False
    for drone in drones:
        if drone.isActive and drone.rect[0] == 150:
            droneCollision = True
        if droneCollision:
            break
    #pygame.Rect.collidelist

    failing= pygame.Rect.colliderect(robot_bullet.rect, cowboy.rect) or \
             pygame.Rect.colliderect(cowboy_bullet[ammo_manager.get_ammo_index()].rect, cowboy.rect) or \
             droneCollision

    if failing:
        cowboy.lose_sound()
        print("collide1")
        pygame.mixer.music.load(lose_noise)
        pygame.mixer.music.play(loops=3, start=0)
        lose_screen = pygame.image.load('lose.png').convert_alpha()
        win.blit(lose_screen, [0, 0])
        print("fail")
        pygame.display.update()
        pygame.time.delay(1000)
        pass
        #pygame.time.delay(1000)

    for drone in drones:
        for bullet in cowboy_bullet:
            if drone.isActive is True and pygame.Rect.colliderect(drone.rect, bullet.rect):
                drone.isActive = False
                canDamage += 1
                print("canDamage : " + str(canDamage))
                #decrease armor image
                pass

    for bodypart in robot.bodyparts:
        for b in cowboy_bullet:
            if pygame.Rect.colliderect(b.rect, bodypart.rect):
                b.reset()
                robot.sound()
                if canDamage == 4:
                    winning = robot.decrease_health(bodypart)
                    print("collide")
                if winning:
                    pygame.mixer.music.load(win_noise)
                    pygame.mixer.music.play(loops=1, start=0)
                    win_screen = pygame.image.load('win.png').convert_alpha()
                    win.blit(win_screen, [0, 0])
                    print("win")
                    pygame.display.update()
                    pygame.time.delay(1000)
                    pass
                    #break
                # pygame.time.delay(1000)

    return winning,failing
    pass

def main():
    will_reset = False
    clock.tick(10)
    pygame.display.set_caption("Cowboy vs. Robot")
    bg1=pygame.image.load("SpaceBackground(Rapid).png").convert_alpha()
    bg2=pygame.image.load("alien_land_v1.png").convert_alpha()

    global drones
    drones = []
    drone_one = Drone(path="drone.png", position=(win_width, 0))
    drone_two = Drone(path="drone.png", position=(1100, 100))
    drone_three = Drone(path="drone.png", position=(win_width, 200))
    drone_four = Drone(path="drone.png", position=(1100, 300))
    drones.append(drone_one)
    drones.append(drone_two)
    drones.append(drone_three)
    drones.append(drone_four)
    for drone in drones:
        if drone.isActive is True:
            drone.draw(win)
        pass

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
    drone_move_counter = 3
    run=True
    while run:
       #pygame.time.delay(50)
       for event in pygame.event.get():
           if ((event.type == pygame.KEYDOWN and event.key == pygame.K_q) or \
                   (event.type == pygame.QUIT)):
               run = False
           elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
               if ammo_manager.try_shoot():
                print(ammo_manager.ammo)
                cowboy_bullet[ammo_manager.get_ammo_index()].shoot(angle)
           elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
               will_reset = True
               run = False

       ammo_manager.update_reload(50)


       winning,failing=detect_collision()
       win.blit(bg1, (0, 0))
       win.blit(bg2, (0, 0))

       if not (winning or failing):
        robot.draw(win)
        cowboy.draw(win)
        for drone in drones:
            if drone.isActive is True:
                drone.draw(win)


        if not (winning or failing) and drone_move_counter == 3:
            for drone in drones:
                if drone.isActive is True:
                    drone.move(drone_speed)
            drone_move_counter = -1
        drone_move_counter += 1

       if not robot_gun.rotate(robot_gun_rot_speed, 320):
           robot_bullet.velocity=(-1, 0) * bullet_speed
           robot_bullet.update_position(bullet_speed)
           pygame.mixer.music.load("RobotLaserSound.wav")
           pygame.mixer.music.play(loops=1, start=0)
           robot_bullet.draw(win)


       if not (winning or failing):
            for b in cowboy_bullet:
                b.update_position(bullet_speed)
                if b.visibility:
                    b.draw(win)


       angle += cowboy_gun_rot_speed


       if not (winning or failing):
            cowboy_gun.rotate(win, angle)
            pygame.display.update()

    if will_reset:
        main()
    
    #pygame.time.delay(100)
    pass

main()