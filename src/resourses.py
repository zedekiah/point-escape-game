import pygame
from msgspec import Struct, field
from pygame.font import Font


class Resourses(Struct):
    _font: Font | None = field(default=None)

    @property
    def font(self) -> Font:
        if self._font is None:
            self._font = pygame.font.SysFont('Arial', 24)
        return self._font


resourses = Resourses()
