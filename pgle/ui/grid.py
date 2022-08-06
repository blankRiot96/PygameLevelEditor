import pygame
from pgle.events import EventBuilder


class GridManager:
    def __init__(self, rect: pygame.Rect, tile_size: int) -> None:
        self.rect = rect
        self.size = rect.size
        self.tile_size = tile_size
        self.boiler_surf = pygame.Surface((tile_size, tile_size))
        self.boiler_surf.fill("red")
        self.boiler_surf.set_alpha(150)
        self.boiler_pos = (0, 0)
        self.draw_surf = False
        self.grid_surf = pygame.Surface(rect.size, pygame.SRCALPHA)

    def update(self, event_builder: EventBuilder) -> None:
        mx, my = event_builder.mouse_pos
        mx, my = mx - self.rect.x, my - self.rect.y
        self.boiler_pos = (
            mx - (mx % self.tile_size),
            my - (my % self.tile_size)
        )
        if self.rect.collidepoint(event_builder.mouse_pos):
            self.draw_surf = True
        else:
            self.draw_surf = False

    def draw(self, screen):
        self.grid_surf.fill("black")
        self.grid_surf.blit(self.boiler_surf, self.boiler_pos)
        screen.blit(self.grid_surf, self.rect)
        for col in range(self.size[0] // self.tile_size):
            coord = (col * self.tile_size)
            pygame.draw.line(screen, "white", self.rect.topleft + pygame.Vector2(coord, 0), self.rect.topleft + pygame.Vector2(coord, self.rect.height))
        for row in range(self.size[1] // self.tile_size):
            coord = (row * self.tile_size)
            pygame.draw.line(screen, "white", self.rect.topleft + pygame.Vector2(0, coord), self.rect.topleft + pygame.Vector2(self.rect.width, coord))
        pygame.draw.rect(screen, "white", self.rect, width=1)


