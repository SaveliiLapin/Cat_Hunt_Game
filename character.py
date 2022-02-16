import pygame
import variables as var


class Character:
    def __init__(self, screen):
        self.image = pygame.image.load('assets/character.png')
        self.rect = self.image.get_rect()
        self.rect.center = (screen.centerx + 1, screen.centery + 1)

    def draw(self):
        var.SCREEN.blit(self.image, self.rect)

    def movement(self, direction, screen):
        if self.rect.left > 16 and direction[0] == -1:
            self.rect.x += direction[0] * 32
        elif self.rect.right < screen.right - 16 and direction[0] == 1:
            self.rect.x += direction[0] * 32
        if self.rect.top > 12 and direction[1] == -1:
            self.rect.y += direction[1] * 24
        elif self.rect.bottom < screen.bottom - 12 and direction[1] == 1:
            self.rect.y += direction[1] * 24
