import pygame
import variables as var
import random as r


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()

        self.image = pygame.image.load('assets/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.left = r.randint(0, 24) * 32 + 2
        self.rect.top = r.randint(0, 24) * 24 + 2

        while abs(self.rect.left - var.CHARACTER.rect.left) < 32 * 4 and abs(self.rect.top - var.CHARACTER.rect.top) < 24 * 4:
            self.rect.left = r.randint(0, 24) * 32 + 2
            self.rect.top = r.randint(0, 24) * 24 + 2

    def draw(self):
        var.SCREEN.blit(self.image, self.rect)

    def movement(self):
        if (var.TICK - 1) % 30 == 0:
            if abs(self.rect.centerx - var.CHARACTER.rect.centerx) > abs(self.rect.centery - var.CHARACTER.rect.centery):
                if self.rect.centerx < var.CHARACTER.rect.centerx:
                    self.rect.x += 32
                elif self.rect.centerx > var.CHARACTER.rect.centerx:
                    self.rect.x -= 32
            else:
                if self.rect.centery < var.CHARACTER.rect.centery:
                    self.rect.y += 24
                elif self.rect.centery > var.CHARACTER.rect.centery:
                    self.rect.y -= 24
