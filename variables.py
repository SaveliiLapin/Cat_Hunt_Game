import pygame
from pygame.sprite import Group
import character as ch

pygame.font.init()
pygame.display.set_caption('Cat Hunt')

FPS = 60
CLOCK = pygame.time.Clock()
TICK = 0

WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN_RECT = SCREEN.get_rect()

IS_NAME = True
IS_MAIN = False
IS_GAME = False
IS_PAUSE = False
IS_LOSE = False
IS_END = False
IS_TOP = False
IS_INSTR = True
SCREEN_CHOICE = 0

# 0 - ввод никнейма
# 1 - главное меню
# 2 - игра
# 3 - пауза
# 4 - проигрыш
# 5 - конец игры
# 6 - топ игроков

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NICKNAME = str()

FONT_18 = pygame.font.Font('assets/2.ttf', 18)
FONT_20 = pygame.font.Font('assets/2.ttf', 20)
FONT_40 = pygame.font.Font('assets/2.ttf', 40)
FONT_100 = pygame.font.Font('assets/2.ttf', 100)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 191, 255)
GREY = (100, 100, 100)
RED = (255, 0, 0)

COLOR_OF_WORDS = GREY
REV_COLOR_OF_WORDS = (255 - COLOR_OF_WORDS[0], 255 - COLOR_OF_WORDS[1], 255 - COLOR_OF_WORDS[2])

NAME_OF_GAME = FONT_100.render('CAT HUNT', False, COLOR_OF_WORDS)
NAME_OF_GAME_RECT = NAME_OF_GAME.get_rect()
NAME_OF_GAME_RECT.center = (WIDTH / 2, 100)

CHARACTER = ch.Character(SCREEN_RECT)
BULLETS = Group()
ENEMIES = Group()

SCORE = 0
TIME_LEFT = 60
