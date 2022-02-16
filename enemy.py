import pygame
import variables as var
import random as r


class Enemy(pygame.sprite.Sprite):
    def __init__(self, character):
        super(Enemy, self).__init__()

        random_x = character.rect.left
        random_y = character.rect.top

        while abs(random_x - character.rect.left) < 32 * 4 and abs(random_y - character.rect.top) < 24 * 4:
            random_x = r.randint(0, 24) * 32 + 2
            random_y = r.randint(0, 24) * 24 + 2

        self.image = pygame.image.load('assets/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.left = random_x
        self.rect.top = random_y
        self.is_dead = False
        self.time_before_death = 89
        self.is_drawn = True

    def draw(self, screen):
        if self.time_before_death % 30 == 0:
            self.is_drawn = not self.is_drawn
        if self.is_dead:
            self.time_before_death -= 1
        if self.is_drawn:
            screen.blit(self.image, self.rect)

    def movement(self, character):
        if (var.TICK - 1) % 30 == 0 and not self.is_dead:
            if abs(self.rect.centerx - character.centerx) > abs(self.rect.centery - character.centery):
                if self.rect.centerx < character.centerx:
                    self.rect.x += 32
                elif self.rect.centerx > character.centerx:
                    self.rect.x -= 32
            else:
                if self.rect.centery < character.centery:
                    self.rect.y += 24
                elif self.rect.centery > character.centery:
                    self.rect.y -= 24
