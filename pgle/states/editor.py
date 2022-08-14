"""
This file is a part of the 'PygameLevelEditor' source code.
The source code is distributed under the MIT license.

This code uses the stages pattern which can be found documented 
in docs/patterns/stages.md
"""

import pygame

from pgle.events import ControlScheme, EventBuilder
from pgle.ui.grid import GridManager
from pgle._types import Controls
import json
from pgle.common import VERSION


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


class SaveStage(EditorGridStage):
    def __init__(self, event_builder) -> None:
        super().__init__(event_builder)
        self.save_scheme = ControlScheme(
            self.event_builer,
            {
                Controls.SINGLE: {
                    "save": [pygame.K_s]
                },
                Controls.HOLD: {}
            }
        )

    def update(self):
        super().update()
        if "save" in self.save_scheme.get_controls():
            save_data = {
                "version": VERSION,
                "layers": self.grid_manager.layers
            }
            with open("test_2.json", "w") as f:
                json.dump(save_data, f)
            raise SystemExit
        

class EditorState(SaveStage):
    pass
