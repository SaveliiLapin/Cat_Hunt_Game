import pygame
import sys
import variables as var
import character as ch
import bullet as bul
import enemy as en
import database as db
import instructions as ins
import dead_enemy as de


def game():
    if var.IS_INSTR:
        ins.instructions()

    score_frame = pygame.Rect(0, 0, 32, 24)

    while var.IS_GAME:
        var.SCREEN.fill(var.REV_COLOR_OF_WORDS)

        if var.TIME_LEFT == 0:
            var.SCREEN_CHOICE = 5
            var.IS_GAME = False
            var.IS_END = True
            var.TICK = 0
            var.TIME_LEFT = 60
            db.write_score()

        for i in range(32, 800, 32):
            pygame.draw.line(var.SCREEN, var.COLOR_OF_WORDS, [i, 0], [i, 600], 2)

        for i in range(24, 600, 24):
            pygame.draw.line(var.SCREEN, var.COLOR_OF_WORDS, [0, i], [800, i], 2)

        for dead_enemy in var.DEADENEMIES:
            if dead_enemy.time_before_death == 0:
                var.DEADENEMIES.remove(dead_enemy)

            dead_enemy.draw()

        for bullet in var.BULLETS:
            bullet.movement()
            bullet.draw()

            if bullet.rect.bottom < var.SCREEN_RECT.top or bullet.rect.top > var.SCREEN_RECT.bottom:
                var.BULLETS.remove(bullet)
            elif bullet.rect.right < var.SCREEN_RECT.left or bullet.rect.left > var.SCREEN_RECT.right:
                var.BULLETS.remove(bullet)

        if var.TICK == 1:
            new_enemy = en.Enemy()
            var.ENEMIES.add(new_enemy)

        for enemy in var.ENEMIES:
            enemy.movement()
            enemy.draw()

            if enemy.rect.centerx == var.CHARACTER.rect.centerx and enemy.rect.centery == var.CHARACTER.rect.centery:
                var.SCREEN_CHOICE = 4
                var.IS_GAME = False
                var.IS_LOSE = True
                var.TICK = 0
                var.TIME_LEFT = 60
                db.write_score()

        ch.Character.draw(var.CHARACTER)
        pygame.draw.rect(var.SCREEN, var.COLOR_OF_WORDS, score_frame)

        score_text = var.FONT_18.render(str(var.SCORE), False, var.REV_COLOR_OF_WORDS)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (score_frame.centerx + 1, score_frame.centery + 1)
        var.SCREEN.blit(score_text, (score_text_rect.left, score_text_rect.top))

        time_text = var.FONT_20.render(str(var.TIME_LEFT), False, var.COLOR_OF_WORDS)
        var.SCREEN.blit(time_text, (var.SCREEN_RECT.centerx - 15, var.SCREEN_RECT.top + 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    ch.Character.movement(var.CHARACTER, (0, -1))
                elif event.key == pygame.K_s:
                    ch.Character.movement(var.CHARACTER, (0, 1))
                elif event.key == pygame.K_a:
                    ch.Character.movement(var.CHARACTER, (-1, 0))
                elif event.key == pygame.K_d:
                    ch.Character.movement(var.CHARACTER, (1, 0))
                elif event.key == pygame.K_UP:
                    new_bullet = bul.Bullet(2)
                    var.BULLETS.add(new_bullet)
                elif event.key == pygame.K_DOWN:
                    new_bullet = bul.Bullet(1)
                    var.BULLETS.add(new_bullet)
                elif event.key == pygame.K_LEFT:
                    new_bullet = bul.Bullet(3)
                    var.BULLETS.add(new_bullet)
                elif event.key == pygame.K_RIGHT:
                    new_bullet = bul.Bullet(4)
                    var.BULLETS.add(new_bullet)
                elif event.key == pygame.K_ESCAPE:
                    var.IS_GAME = False
                    var.IS_PAUSE = True
                    var.SCREEN_CHOICE = 3

        if var.TICK >= var.FPS * 2 + 1 and var.IS_GAME:
            var.TICK = 0

        hits = pygame.sprite.groupcollide(var.ENEMIES, var.BULLETS, True, True)
        for hit in hits:
            var.SCORE += 1
            new_dead_enemy = de.DeadEnemy(hit.rect.left, hit.rect.top)
            var.DEADENEMIES.add(new_dead_enemy)

        if var.TICK == 1 or var.TICK == 61:
            var.TIME_LEFT -= 1

        var.TICK += 1
        pygame.display.flip()
        var.CLOCK.tick(var.FPS)
