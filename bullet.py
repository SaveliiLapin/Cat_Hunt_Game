import pygame
import variables as var


class Bullet(pygame.sprite.Sprite):
    def __init__(self, direction):
        super(Bullet, self).__init__()
        self.direction = direction
        self.image = pygame.image.load('assets/bone.png')
        if self.direction == 1 or self.direction == 2:
            self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.center = (var.CHARACTER.rect.centerx + 1, var.CHARACTER.rect.centery + 1)

    def draw(self):
        var.SCREEN.blit(self.image, self.rect)

    def movement(self):
        if self.direction == 1:
            self.rect.y += 10
        elif self.direction == 2:
            self.rect.y -= 10
        elif self.direction == 3:
            self.rect.x -= 10
        elif self.direction == 4:
            self.rect.x += 10
