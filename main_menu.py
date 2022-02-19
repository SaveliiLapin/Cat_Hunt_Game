import pygame
import sys
import variables as var


def main_menu():
    start = var.FONT_40.render('Start', False, var.COLOR_OF_WORDS)
    start_rect = start.get_rect()
    start_rect.center = (var.WIDTH / 2, 200)

    top_players = var.FONT_40.render('Top players', False, var.COLOR_OF_WORDS)
    top_players_rect = top_players.get_rect()
    top_players_rect.center = (var.WIDTH / 2, 300)

    exitt = var.FONT_40.render('Exit', False, var.COLOR_OF_WORDS)
    exitt_rect = exitt.get_rect()
    exitt_rect.center = (var.WIDTH / 2, 400)

    select = var.FONT_18.render('Use arrows to select', False, var.COLOR_OF_WORDS)
    select_rect = select.get_rect()
    select_rect.center = (var.WIDTH / 2, 500)

    frame_of_choice = pygame.Rect(start_rect.left - 5, start_rect.top - 5, start_rect.width + 10, start_rect.height + 10)

    while var.IS_MAIN:
        var.SCREEN.fill(var.REV_COLOR_OF_WORDS)
        var.SCREEN.blit(var.NAME_OF_GAME, (var.NAME_OF_GAME_RECT.left, var.NAME_OF_GAME_RECT.top))

        if frame_of_choice.center == start_rect.center:
            start = var.FONT_40.render('Start', False, var.REV_COLOR_OF_WORDS)
            top_players = var.FONT_40.render('Top players', False, var.COLOR_OF_WORDS)
            exitt = var.FONT_40.render('Exit', False, var.COLOR_OF_WORDS)
            frame_of_choice = pygame.Rect(start_rect.left - 5, start_rect.top - 5, start_rect.width + 10, start_rect.height + 10)
        elif frame_of_choice.center == top_players_rect.center:
            start = var.FONT_40.render('Start', False, var.COLOR_OF_WORDS)
            top_players = var.FONT_40.render('Top players', False, var.REV_COLOR_OF_WORDS)
            exitt = var.FONT_40.render('Exit', False, var.COLOR_OF_WORDS)
            frame_of_choice = pygame.Rect(top_players_rect.left - 5, top_players_rect.top - 5, top_players_rect.width + 10, top_players_rect.height + 10)
        else:
            start = var.FONT_40.render('Start', False, var.COLOR_OF_WORDS)
            top_players = var.FONT_40.render('Top players', False, var.COLOR_OF_WORDS)
            exitt = var.FONT_40.render('Exit', False, var.REV_COLOR_OF_WORDS)
            frame_of_choice = pygame.Rect(exitt_rect.left - 5, exitt_rect.top - 5, exitt_rect.width + 10, exitt_rect.height + 10)

        pygame.draw.rect(var.SCREEN, var.COLOR_OF_WORDS, frame_of_choice)
        var.SCREEN.blit(start, (start_rect.left, start_rect.top))
        var.SCREEN.blit(top_players, (top_players_rect.left, top_players_rect.top))
        var.SCREEN.blit(exitt, (exitt_rect.left, exitt_rect.top))
        var.SCREEN.blit(select, (select_rect.left, select_rect.top))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and frame_of_choice.top < exitt_rect.top - 5:
                    frame_of_choice.top += 100
                elif event.key == pygame.K_UP and frame_of_choice.top > start_rect.top + 5:
                    frame_of_choice.top -= 100
                elif event.key == pygame.K_RETURN:
                    if frame_of_choice.center == exitt_rect.center:
                        sys.exit()
                    elif frame_of_choice.center == top_players_rect.center:
                        var.IS_MAIN = False
                        var.IS_TOP = True
                        var.SCREEN_CHOICE = 6
                    elif frame_of_choice.center == start_rect.center:
                        var.IS_MAIN = False
                        var.IS_GAME = True
                        var.SCREEN_CHOICE = 2

        pygame.display.flip()
        var.CLOCK.tick(var.FPS)
