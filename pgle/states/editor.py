import pygame
from pgle.ui.grid import GridManager
from pgle.events import EventBuilder


class EditorInitStage:
    def __init__(self, event_builder: EventBuilder) -> None:
        self.event_builer = event_builder


class EditorGridStage(EditorInitStage):
    def __init__(self, event_builder) -> None:
        super().__init__(event_builder)
        grid_rect = pygame.Rect((1100 - 780, 30), (750, 450))
        self.grid_manager = GridManager(grid_rect, 50)

    def update(self):
        self.grid_manager.update(self.event_builer)

    def draw(self, screen):
        self.grid_manager.draw(screen)


class EditorState(EditorGridStage):
    pass
