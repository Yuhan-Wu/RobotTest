import pygame
pygame.init()

from GunBulletTest.Gun import Gun
from GunBulletTest.Bullet import Bullet

#VARIABLES
screen_width = 1200
screen_height = 600
clock = pygame.time.Clock()

def main():
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    #GLOBAL VARIABLES FOR WINNING AND FAILING
    global win_state, fail_state
    win_state = False
    fail_state = False

    #DRAWING THE GUN
    global gun
    gun_image_path = "D:\Semester 1 - Rapid Prototyping\Team 1 Works\GunBulletTest\gun.png"
    gun_position = (300, 400)
    gun = Gun(gun_image_path, gun_position)
    #gun.draw(screen)

    #DRAWING THE BULLET
    global bullet
    bullet_image_path = "D:\Semester 1 - Rapid Prototyping\Team 1 Works\GunBulletTest\projectile.png"
    bullet_position = (300, 400)
    bullet = Bullet(bullet_image_path, bullet_position)
    #bullet.draw(screen)

    #MAIN LOOP
    run = True
    isRotate = True
    angle = 0
    velocity = 20
    while run:
        pygame.time.delay(100)
        #clock.tick(60)

        for event in pygame.event.get():
            if ((event.type == pygame.KEYDOWN and event.key == pygame.K_q) or (event.type == pygame.QUIT)):
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                isRotate = False

        screen.fill(0)

        if isRotate:
            angle += 10
            pass
        else:
            bullet.move(screen, angle, velocity)
            pass
        #bullet.draw(screen)
        gun.rotate(screen, angle)

        #pygame.display.update()
        pygame.display.flip()
        #gun.draw(screen)

    pygame.quit()
