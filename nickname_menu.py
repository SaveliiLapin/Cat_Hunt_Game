import pygame
import sys
import variables as var

pygame.init()


def name_menu():
    is_line = True
    enter_name = var.FONT_40.render('Enter your name:', False, var.COLOR_OF_WORDS)
    enter_name_rect = enter_name.get_rect()
    enter_name_rect.center = (var.WIDTH / 2, 300)

    enter = var.FONT_18.render('Press enter to continue', False, var.COLOR_OF_WORDS)
    enter_rect = enter.get_rect()
    enter_rect.center = (var.WIDTH / 2, 500)

    frame_of_name = pygame.Rect(225, 350, 350, 50)

    line = var.FONT_40.render('|', False, var.REV_COLOR_OF_WORDS)
    line_rect = line.get_rect()

    while var.IS_NAME:
        var.SCREEN.fill(var.REV_COLOR_OF_WORDS)
        var.SCREEN.blit(var.NAME_OF_GAME, (var.NAME_OF_GAME_RECT.left, var.NAME_OF_GAME_RECT.top + 50))
        var.SCREEN.blit(enter_name, (enter_name_rect.left, enter_name_rect.top))
        pygame.draw.rect(var.SCREEN, var.COLOR_OF_WORDS, frame_of_name)

        input_text = var.FONT_40.render(var.NICKNAME, False, var.REV_COLOR_OF_WORDS)
        input_text_rect = input_text.get_rect()
        input_text_rect.center = (frame_of_name.centerx - line_rect.width / 2, frame_of_name.centery)
        var.SCREEN.blit(input_text, (input_text_rect.left, input_text_rect.top))

        if is_line:
            var.SCREEN.blit(line, (input_text_rect.right, input_text_rect.top))

        if len(var.NICKNAME) > 0:
            var.SCREEN.blit(enter, (enter_rect.left, enter_rect.top))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(var.NICKNAME) > 0:
                    var.SCREEN_CHOICE = 1
                    var.TICK = 0
                    var.IS_NAME = False
                    var.IS_MAIN = True
                elif 96 < event.key < 123 and len(var.NICKNAME) < 9:
                    var.NICKNAME += var.ALPHABET[event.key - 97]
                elif event.key == pygame.K_BACKSPACE:
                    var.NICKNAME = var.NICKNAME[:-1]

        var.TICK += 1

        if var.TICK == var.FPS + 1:
            var.TICK = 1
        elif var.TICK % (var.FPS / 2) == 0:
            is_line = not is_line

        var.CLOCK.tick(var.FPS)
