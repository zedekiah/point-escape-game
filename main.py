from types import SimpleNamespace

import pygame

from src.constants import COLOR_BLACK
from src.core import main_loop

settings = SimpleNamespace(
    screen_width=800,
    screen_height=600,
    background_color=COLOR_BLACK,
    player_speed=5,
)


def main() -> None:
    pygame.init()

    main_loop(settings)
    print('Досвидули!')


if __name__ == '__main__':
    main()
