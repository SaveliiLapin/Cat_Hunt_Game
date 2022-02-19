import pygame
import sys
import variables as var


def pause():
    resume = var.FONT_40.render('Continue', False, var.COLOR_OF_WORDS)
    resume_rect = resume.get_rect()
    resume_rect.center = (var.WIDTH / 2, 300)

    main_menu = var.FONT_40.render('Main menu', False, var.COLOR_OF_WORDS)
    main_menu_rect = main_menu.get_rect()
    main_menu_rect.center = (var.WIDTH / 2, 400)
    frame_of_choice = pygame.Rect(resume_rect.left - 5, resume_rect.top - 5, resume_rect.width + 10, resume_rect.height + 10)

    while var.IS_PAUSE:
        var.SCREEN.fill(var.REV_COLOR_OF_WORDS)
        var.SCREEN.blit(var.NAME_OF_GAME, (var.NAME_OF_GAME_RECT.left, var.NAME_OF_GAME_RECT.top))

        if frame_of_choice.center == resume_rect.center:
            resume = var.FONT_40.render('Continue', False, var.REV_COLOR_OF_WORDS)
            main_menu = var.FONT_40.render('Main menu', False, var.COLOR_OF_WORDS)
            frame_of_choice = pygame.Rect(resume_rect.left - 5, resume_rect.top - 5, resume_rect.width + 10, resume_rect.height + 10)
        elif frame_of_choice.center == main_menu_rect.center:
            resume = var.FONT_40.render('Continue', False, var.COLOR_OF_WORDS)
            main_menu = var.FONT_40.render('Main menu', False, var.REV_COLOR_OF_WORDS)
            frame_of_choice = pygame.Rect(main_menu_rect.left - 5, main_menu_rect.top - 5, main_menu_rect.width + 10, main_menu_rect.height + 10)

        pygame.draw.rect(var.SCREEN, var.COLOR_OF_WORDS, frame_of_choice)
        var.SCREEN.blit(resume, (resume_rect.left, resume_rect.top))
        var.SCREEN.blit(main_menu, (main_menu_rect.left, main_menu_rect.top))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and frame_of_choice.top < main_menu_rect.top - 5:
                    frame_of_choice.y += 100
                elif event.key == pygame.K_UP and frame_of_choice.top > resume_rect.top + 5:
                    frame_of_choice.y -= 100
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
                        var.IS_PAUSE = False
                        var.TICK = 0
                        var.TIME_LEFT = 60
                        var.SCREEN_CHOICE = 1

                    elif frame_of_choice.center == resume_rect.center:
                        var.IS_PAUSE = False
                        var.IS_GAME = True
                        var.SCREEN_CHOICE = 2
        pygame.display.flip()
        var.CLOCK.tick(var.FPS)
