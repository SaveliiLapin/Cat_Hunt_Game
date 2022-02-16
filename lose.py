import pygame
import sys
import variables as var


def lose():
    retry = var.FONT_40.render('Retry', False, var.COLOR_OF_WORDS)
    retry_rect = retry.get_rect()
    retry_rect.center = (var.WIDTH / 2, 300)

    main_menu = var.FONT_40.render('Main menu', False, var.COLOR_OF_WORDS)
    main_menu_rect = main_menu.get_rect()
    main_menu_rect.center = (var.WIDTH / 2, 400)
    rect_position_y = retry_rect.top - 5
    frame_of_choice = pygame.Rect(retry_rect.left - 5, rect_position_y, retry_rect.width + 10, retry_rect.height + 10)

    lost = var.FONT_40.render('Your score:' + str(var.SCORE), False, var.COLOR_OF_WORDS)
    lost_rect = lost.get_rect()
    lost_rect.center = (var.WIDTH / 2, 200)

    while var.IS_LOSE:
        var.SCREEN.fill(var.REV_COLOR_OF_WORDS)
        var.SCREEN.blit(var.NAME_OF_GAME, (var.NAME_OF_GAME_RECT.left, var.NAME_OF_GAME_RECT.top))

        if frame_of_choice.center == retry_rect.center:
            retry = var.FONT_40.render('Retry', False, var.REV_COLOR_OF_WORDS)
            main_menu = var.FONT_40.render('Main menu', False, var.COLOR_OF_WORDS)
            frame_of_choice = pygame.Rect(retry_rect.left - 5, rect_position_y, retry_rect.width + 10, retry_rect.height + 10)
        elif frame_of_choice.center == main_menu_rect.center:
            retry = var.FONT_40.render('Retry', False, var.COLOR_OF_WORDS)
            main_menu = var.FONT_40.render('Main menu', False, var.REV_COLOR_OF_WORDS)
            frame_of_choice = pygame.Rect(main_menu_rect.left - 5, rect_position_y, main_menu_rect.width + 10, main_menu_rect.height + 10)

        var.SCREEN.blit(lost, (lost_rect.left, lost_rect.top))
        pygame.draw.rect(var.SCREEN, var.COLOR_OF_WORDS, frame_of_choice)
        var.SCREEN.blit(retry, (retry_rect.left, retry_rect.top))
        var.SCREEN.blit(main_menu, (main_menu_rect.left, main_menu_rect.top))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and rect_position_y < main_menu_rect.top - 5:
                    rect_position_y += 100
                elif event.key == pygame.K_UP and rect_position_y > retry_rect.top + 5:
                    rect_position_y -= 100
                elif event.key == pygame.K_RETURN:
                    if frame_of_choice.center == main_menu_rect.center:
                        var.CHARACTER.rect.centerx = var.SCREEN_RECT.centerx + 1
                        var.CHARACTER.rect.centery = var.SCREEN_RECT.centery + 1
                        var.SCORE = 0

                        for bullet in var.BULLETS:
                            var.BULLETS.remove(bullet)

                        for enemy in var.ENEMIES:
                            var.ENEMIES.remove(enemy)

                        var.IS_MAIN = True
                        var.IS_LOSE = False
                        var.SCORE = 0
                        var.SCREEN_CHOICE = 1

                    elif frame_of_choice.center == retry_rect.center:
                        var.CHARACTER.rect.centerx = var.SCREEN_RECT.centerx + 1
                        var.CHARACTER.rect.centery = var.SCREEN_RECT.centery + 1
                        var.TICK = 0

                        for bullet in var.BULLETS:
                            var.BULLETS.remove(bullet)

                        for enemy in var.ENEMIES:
                            var.ENEMIES.remove(enemy)

                        var.IS_LOSE = False
                        var.IS_GAME = True
                        var.SCORE = 0
                        var.SCREEN_CHOICE = 2

        pygame.display.flip()
