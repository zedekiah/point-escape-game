from random import randint
from types import SimpleNamespace

import pygame

settings = SimpleNamespace(
    screen_width=800,
    screen_height=600,
    background_color=(0, 0, 0),
    player_speed=5,
)


class Object:
    def __init__(self, x, y, width=50, height=50, color=(255, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height

    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0)

    def set_x(self, value):
        self.x = value
        self.rect.x = value

    def set_y(self, value):
        self.y = value
        self.rect.y = value


# width - ширина
# heigth - высота
# plus - плюс
# equal - равно


def main_loop():
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 24)
    score = 0

    player = Object(300, 300)

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

        text_surface = font.render(f'Очки: {score}', True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))

        pygame.display.flip()

        clock.tick(30)


def main():
    pygame.init()

    main_loop()
    print('Досвидули!')


if __name__ == '__main__':
    main()
    # test()
