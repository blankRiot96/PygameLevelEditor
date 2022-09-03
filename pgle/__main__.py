"""
This file is a part of the 'PygameLevelEditor' source code.
The source code is distributed under the MIT license.
"""

import pygame

from pgle._types import Controls
from pgle.events import ControlScheme, EventBuilder
from pgle.states.editor import EditorState


surf = pygame.Surface((50, 50), pygame.SRCALPHA)
surf.fill("red")
surf.set_alpha(150)
pygame.image.save(surf, "assets/default_tile.png")


class Game:
    """Handles all game related events."""

    SIZE = 1100, 600
    FLAGS = 0

    def __init__(self) -> None:
        pygame.init()
        self._screen = pygame.display.set_mode(self.SIZE, self.FLAGS)
        pygame.display.set_caption("Pygame Level Editor | Editor")
        pygame.display.set_icon(pygame.image.load("assets/logo.png"))
        self._is_running = True
        self.event_builder = EventBuilder()
        self.exit_scheme = ControlScheme(
            self.event_builder,
            {
                Controls.SINGLE: {"quit": [pygame.QUIT, pygame.K_ESCAPE]},
                Controls.HOLD: {},
            },
        )
        self.state = EditorState(self.event_builder)

    def _update(self) -> None:
        self.event_builder.build()
        if "quit" in self.exit_scheme.get_controls():
            self._is_running = False

        self.state.update()

    def _draw(self) -> None:
        self._screen.fill("black")
        self.state.draw(self._screen)
        pygame.display.flip()

    def run(self) -> None:
        while self._is_running:
            self._update()
            self._draw()


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
