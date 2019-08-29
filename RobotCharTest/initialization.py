import pygame
import random
pygame.init()

from RobotCharTest.Robot import Robot
from RobotCharTest.Head import Head
from RobotCharTest.Body import Body
from RobotCharTest.Gun import Gun
from RobotCharTest.Cowboy import Cowboy
from RobotCharTest.RobotGun import RobotGun
from RobotCharTest.Bullet import Bullet
from RobotCharTest.AmmoManager import AmmoManager
from RobotCharTest.AudioManager import AudioManager
from RobotCharTest.ScoreBoard import ScoreBoard
from RobotCharTest.Drone import Drone


win_width=1600
win_height=900
win=pygame.display.set_mode((win_width,win_height))

win_noise = 'WinSound.wav'
lose_noise = 'LoseSound.wav'

clock = pygame.time.Clock()
key=None
global will_restart
will_restart = False

# CONFIG PARAMETER
bullet_speed = 30
cowboy_gun_rot_speed = 10
robot_gun_rot_speed = 0
drone_speed = 8
bullet_damage = -1
ammo_capacity = 6
reloading_time = 20
# CONFIG END

def detect_collision():
    winning = False
    failing = False

    for drone in drones:
        for bullet in cowboy_bullet:
            if pygame.Rect.colliderect(drone.rect, bullet.rect):
                if drone.damage(bullet_damage):
                    sb.add_score(1)
                bullet.reset()
                AudioManager.play("RobotSmash.wav")
                pass
        if pygame.Rect.colliderect(drone.rect, cowboy.rect):
            failing = True

    for bullet in cowboy_bullet:
        if pygame.Rect.colliderect(cowboy.rect, bullet.rect):
            failing = True
    # for bodypart in robot.bodyparts:
    #     for b in cowboy_bullet:
    #         if pygame.Rect.colliderect(b.rect, bodypart.rect):
    #             b.reset()
    #             robot.sound()
    #             if canDamage == 4:
    #                 winning = robot.decrease_health(bodypart)
    #                 print("collide")
    #             if winning:
    #                 pygame.mixer.music.load(win_noise)
    #                 pygame.mixer.music.play(loops=1, start=0)
    #                 win_screen = pygame.image.load('win.png').convert_alpha()
    #                 win.blit(win_screen, [0, 0])
    #                 print("win")
    #                 pygame.display.update()
    #                 pygame.time.delay(1000)
    #                 pass

    return winning,failing
    pass

def main():
    will_restart = False
    clock.tick(10)
    pygame.display.set_caption("Space Spinning Cowboy")
    bg1=pygame.image.load("background_v1.png").convert_alpha()
    bg2=pygame.image.load("alien_land_v1.png").convert_alpha()

    global drones
    drones = []
    drone_one = Drone(path="drone.png", position=(win_width + 100, win_height / 2 - 200))
    drone_two = Drone(path="drone.png", position=(win_width + 1000, win_height / 2 - 100))
    drone_three = Drone(path="drone.png", position=(win_width + 800, win_height / 2 + 100))
    drone_four = Drone(path="drone.png", position=(win_width + 2000, win_height / 2 + 200))
    drones.append(drone_one)
    drones.append(drone_two)
    drones.append(drone_three)
    drones.append(drone_four)
    for drone in drones:
        drone.velocity = (-1, 0)

    # global robot
    # head=Head(path="robot_head_v1.png",position=(win_width-300,win_height-200))
    # body=Body(path="robot_body_v1.png",position=(win_width-300,win_height-160))
    # robot_gun=RobotGun(path="robot_cannon_v1.png",position=(win_width-270,win_height-160))
    # bodyparts=[]
    # bodyparts.append(head)
    # bodyparts.append(body)
    # bodyparts.append(robot_gun)
    # robot=Robot(bodyparts)
    # robot.draw(win)

    global cowboy
    cowboy = Cowboy("cowboy_v1.png", (200, win_height/2-200))
    cowboy_hand = pygame.image.load("cowboy_hand_v1.png").convert_alpha()
    cowboy.draw(win)

    global cowboy_gun
    gun_image_path = "gun_v1.png"
    cowboy_gun_position = (cowboy.rect.topleft[0]+215, cowboy.rect.topleft[1]+80)
    cowboy_gun = Gun(gun_image_path, cowboy_gun_position)
    cowboy_gun.draw(win)

    global ammo_manager
    ammo_manager = AmmoManager(ammo_capacity, reloading_time)

    global cowboy_bullet
    bullet_image_path = "robot_bullet_v1.png"
    cowboy_bullet = []
    counter = ammo_manager.ammo_capacity

    global sb
    sb = ScoreBoard((100, 100))

    while counter > 0:
        b = Bullet(bullet_image_path, (cowboy.rect.topleft[0]+250, cowboy.rect.topleft[1]+40))
        cowboy_bullet.append(b)
        counter -= 1

    # global robot_bullet
    # robot_bullet=Bullet(bullet_image_path, position=(win_width-270,win_height-120))
    # robot_bullet.draw(win)

    cowboy_gun_angle = random.randint(0, 360)

    run = True
    while run:
        for event in pygame.event.get():
            if ((event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or \
                   (event.type == pygame.QUIT)):
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if ammo_manager.try_shoot():
                    cowboy_bullet[ammo_manager.get_ammo_index()].shoot(cowboy_gun_angle)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                will_restart = True
                run = False

        ammo_manager.update_reload(50)

        win.blit(bg1, (0, 0))
        win.blit(bg2, (0, 0))

        winning, failing = detect_collision()

        # Draw
        if not (winning or failing):
            sb.draw(win)
            cowboy.draw(win)
            win.blit(cowboy_hand, (cowboy.rect.topleft[0] + 130, cowboy.rect.topleft[1] + 60))
            cowboy_gun_angle += cowboy_gun_rot_speed
            cowboy_gun.rotate(win, cowboy_gun_angle)
            # Drone
            for drone in drones:
                if drone.isActive:
                    drone.update_position(drone_speed)
                    drone.draw(win)
            # Cowboy Bullet
            for b in cowboy_bullet:
                b.update_position(bullet_speed)
                if b.visibility:
                    b.draw(win)
        elif failing:
            cowboy.lose_sound()
            pygame.mixer.music.load(lose_noise)
            pygame.mixer.music.play(loops=1, start=0)
            lose_screen = pygame.image.load('lose.png').convert_alpha()
            win.blit(lose_screen, [0, 0])
        else:
            pass

        pygame.display.update()
        # if not robot_gun.rotate(robot_gun_rot_speed, 320):
        #     robot_bullet.velocity=(-1, 0) * bullet_speed
        #     robot_bullet.update_position(bullet_speed)
        #     pygame.mixer.music.load("RobotLaserSound.wav")
        #     pygame.mixer.music.play(loops=1, start=0)
        #     robot_bullet.draw(win)

    if will_restart:
        main()
    pass

main()