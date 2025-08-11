from random import randint
from types import SimpleNamespace

import pygame

from .object import Object
from .resourses import resourses


def main_loop(settings: SimpleNamespace) -> None:
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    clock = pygame.time.Clock()
    score = 0

    player = Object(300, 300, title='P1')

    objects = [
        player,
    ]

    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False

            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                cursor_x, cursor_y = e.pos

                if player.x <= cursor_x <= player.x + player.width and player.y <= cursor_y <= player.y + player.height:
                    score += 1
                    player.set_x(randint(0, settings.screen_width - player.width))
                    player.set_y(randint(0, settings.screen_height - player.height))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            player.set_x(player.x + settings.player_speed)
        if keys[pygame.K_UP]:
            player.set_y(player.y - settings.player_speed)
        if keys[pygame.K_LEFT]:
            player.set_x(player.x - settings.player_speed)
        if keys[pygame.K_DOWN]:
            player.set_y(player.y + settings.player_speed)
        screen.fill(settings.background_color)

        for obj in objects:
            obj.render(screen)

        text_surface = resourses.font.render(f'Очки: {score}', True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))

        pygame.display.flip()

        clock.tick(30)
