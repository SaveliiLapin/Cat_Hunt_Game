import pygame
import sys
import variables as var


def instructions():

    start = var.FONT_40.render('Start', False, var.REV_COLOR_OF_WORDS)
    start_rect = start.get_rect()
    start_rect.center = (var.WIDTH / 2, 500)
    frame_of_choice = pygame.Rect(start_rect.left - 5, start_rect.top - 5, start_rect.width + 10, start_rect.height + 10)

    movement = var.FONT_20.render('Use W, A, S, D to move', False, var.COLOR_OF_WORDS)
    movement_rect = movement.get_rect()
    movement_rect.center = (var.WIDTH / 2, 200)

    shoot = var.FONT_20.render('Use arrows to shoot', False, var.COLOR_OF_WORDS)
    shoot_rect = shoot.get_rect()
    shoot_rect.center = (var.WIDTH / 2, 250)

    aim = var.FONT_20.render('Your aim is to kill as many enemies', False, var.COLOR_OF_WORDS)
    aim_rect = aim.get_rect()
    aim_rect.center = (var.WIDTH / 2, 300)

    aim_2 = var.FONT_20.render('as possible in 60 sec', False, var.COLOR_OF_WORDS)
    aim_2_rect = aim_2.get_rect()
    aim_2_rect.center = (var.WIDTH / 2, 350)

    while var.IS_INSTR:
        var.SCREEN.fill(var.REV_COLOR_OF_WORDS)
        var.SCREEN.blit(var.NAME_OF_GAME, (var.NAME_OF_GAME_RECT.left, var.NAME_OF_GAME_RECT.top))
        pygame.draw.rect(var.SCREEN, var.COLOR_OF_WORDS, frame_of_choice)
        var.SCREEN.blit(start, (start_rect.left, start_rect.top))
        var.SCREEN.blit(movement, (movement_rect.left, movement_rect.top))
        var.SCREEN.blit(shoot, (shoot_rect.left, shoot_rect.top))
        var.SCREEN.blit(aim, (aim_rect.left, aim_rect.top))
        var.SCREEN.blit(aim_2, (aim_2_rect.left, aim_2_rect.top))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    var.IS_INSTR = False

        pygame.display.flip()

        var.CLOCK.tick(var.FPS)
