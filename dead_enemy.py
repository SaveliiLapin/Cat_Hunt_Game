import pygame
import variables as var


class DeadEnemy(pygame.sprite.Sprite):
    def __init__(self, left, top):
        super(DeadEnemy, self).__init__()

        self.image = pygame.image.load('assets/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.time_before_death = 60
        self.is_drawn = True

    def draw(self):
        if self.time_before_death % 30 == 0:
            self.is_drawn = not self.is_drawn
        if self.is_drawn:
            var.SCREEN.blit(self.image, self.rect)
        self.time_before_death -= 1
