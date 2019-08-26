import pygame
class Gun(pygame.sprite.Sprite):
    def __init__(self, path, position):
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        pass

    def rotate(self, screen, angle):
        #VARIABLES
        image = self.image
        position = self.rect.topleft
        width, height = self.image.get_size()
        origin_position = (width / 2, height / 2)

        #BOUNDING BOX
        box_around_image = [pygame.math.Vector2(p) for p in [(0, 0), (width, 0), (width, -height), (0, -height)]]
        box_rotate = [p.rotate(angle) for p in box_around_image]
        min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

        #TRANSLATION OF PIVOT
        pivot = pygame.math.Vector2(origin_position[0], -origin_position[1])
        pivot_rotate = pivot.rotate(angle)
        pivot_move = pivot_rotate - pivot

        #CALCULATE UPPER LEFT CORNER OF IMAGE
        origin = (position[0] - origin_position[0] + min_box[0] - pivot_move[0], position[1] - origin_position[1] - max_box[1] + pivot_move[1])

        #GET A ROTATED IMAGE
        rotated_image = pygame.transform.rotate(self.image, angle)

        #DRAW A RECTANGLE AROUND THE IMAGE
        #pygame.draw.rect(screen, (255, 0, 0), (*origin, *rotated_image.get_size()), 2)

        #BLIT THE IMAGE
        screen.blit(rotated_image, origin)
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pass



