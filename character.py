import pygame
import variables as var


class Character:
    def __init__(self):
        self.image = pygame.image.load('assets/character.png')
        self.rect = self.image.get_rect()
        self.rect.center = (var.SCREEN_RECT.centerx + 1, var.SCREEN_RECT.centery + 1)

    def draw(self):
        var.SCREEN.blit(self.image, self.rect)

    def movement(self, direction):
        if self.rect.left > 16 and direction[0] == -1:
            self.rect.x += direction[0] * 32
        elif self.rect.right < var.SCREEN_RECT.right - 16 and direction[0] == 1:
            self.rect.x += direction[0] * 32
        if self.rect.top > 12 and direction[1] == -1:
            self.rect.y += direction[1] * 24
        elif self.rect.bottom < var.SCREEN_RECT.bottom - 12 and direction[1] == 1:
            self.rect.y += direction[1] * 24
