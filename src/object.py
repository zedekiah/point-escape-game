import pygame
from pygame import Surface

from .constants import COLOR_RED, COLOR_WHITE
from .resourses import resourses
from .typing import Color


class Object:
    def __init__(
        self,
        x: int,
        y: int,
        width: int = 50,
        height: int = 50,
        color: Color = COLOR_RED,
        title: str | None = None,
    ) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.title = title
        self.title_surface = resourses.font.render(self.title, True, COLOR_WHITE)

    def render(self, surface: Surface) -> None:
        pygame.draw.rect(surface, self.color, self.rect, 0)
        if self.title:
            self.render_title(surface)

    def render_title(self, surface: Surface) -> None:
        surface.blit(
            self.title_surface,
            (
                self.x + self.width / 2 - self.title_surface.get_width() / 2,
                self.y + self.height / 2 - self.title_surface.get_height() / 2,
            ),
        )

    def set_x(self, value: int) -> None:
        self.x = value
        self.rect.x = value

    def set_y(self, value: int) -> None:
        self.y = value
        self.rect.y = value
