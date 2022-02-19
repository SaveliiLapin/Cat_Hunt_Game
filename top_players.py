import pygame
import sys
import variables as var
import sqlite3 as sq


def top_players():
    with sq.connect('assets/top_users.db') as con:
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS top_users (name TEXT, score INTEGER)')
        cur.execute('SELECT * FROM top_users ORDER BY score DESC LIMIT 5')
        ans = cur.fetchall()

    back = var.FONT_40.render('Back', False, var.REV_COLOR_OF_WORDS)
    back_rect = back.get_rect()
    back_rect.center = (var.WIDTH / 2, 500)
    frame_of_choice = pygame.Rect(back_rect.left - 5, back_rect.top - 5, back_rect.width + 10, back_rect.height + 10)

    while var.IS_TOP:
        var.SCREEN.fill(var.REV_COLOR_OF_WORDS)
        var.SCREEN.blit(var.NAME_OF_GAME, (var.NAME_OF_GAME_RECT.left, var.NAME_OF_GAME_RECT.top))
        pygame.draw.rect(var.SCREEN, var.COLOR_OF_WORDS, frame_of_choice)
        var.SCREEN.blit(back, (back_rect.left, back_rect.top))

        for i in range(len(ans)):
            player = var.FONT_40.render(ans[i][0] + ' ' + str(ans[i][1]), False, var.COLOR_OF_WORDS)
            player_rect = player.get_rect()
            player_rect.center = (var.WIDTH / 2, 200 + i * 50)
            var.SCREEN.blit(player, (player_rect.left, player_rect.top))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    var.IS_TOP = False
                    var.IS_MAIN = True
                    var.SCREEN_CHOICE = 1

        pygame.display.flip()
        var.CLOCK.tick(var.FPS)
