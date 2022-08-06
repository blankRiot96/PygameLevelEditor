"""
This file is a part of the 'PygameLevelEditor' source code.
The source code is distributed under the MIT license.

Has all classes and components for the User Interface 
in relation to the grid element of the editor.
"""

import pygame

from pgle._types import Pos
from pgle.events import EventBuilder


class ControlBlock:
    """Places/Deletes blocks.

    This block allows you to place/delete any given tile, or object.
    """

    def __init__(self, tile_size: int, grid_rect: pygame.Rect) -> None:
        """Constructor of the ControlBlock class.

        Args:
            tile_size (int): The size of the tile.
            grid_rect (pygame.Rect): The size and position of the overall grid area.

        Returns:
            None
        """
        self._grid_rect = grid_rect
        self._size = tile_size
        self.surf = pygame.Surface((tile_size, tile_size))
        self.surf.fill("red")
        self.surf.set_alpha(150)
        self.rect = self.surf.get_rect()
        self._is_visible = False

    def update(self, mouse_pos: Pos) -> None:
        """Updates the ControlBlock.

        This takes the position of the mouse within the window,
        and converts it to the position relative to the area of the grid.
        Handles visibility as well. (Visible only if cursor within the grid area)

        Args:
            mouse_pos (Pos): The position of the mouse within the window.

        Returns:
            None
        """
        mx, my = mouse_pos
        mx, my = mx - self._grid_rect.x, my - self._grid_rect.y
        self.rect.topleft = (mx - (mx % self._size), my - (my % self._size))
        self._is_visible = self._grid_rect.collidepoint(mouse_pos)

    def draw(self, screen: pygame.Surface) -> None:
        """Draws the ControlBlock if visible.

        Args:
            screen (pygame.Surface): Surface to draw on.

        Returns:
            None
        """
        if self._is_visible:
            screen.blit(self.surf, self.rect)


class GridManager:
    """Handles the Grid element.

    Allows you to place/remove tiles/blocks in your level.

    Attributes:
        rect (pygame.Rect): Information on the position and size
        of the grid area.
        surf (pygame.Surface): Surface of the grid element.
        tile_size (int): Size of each tile.
    """

    def __init__(self, rect: pygame.Rect, tile_size: int) -> None:
        """Constructor of the GridManager class.

        Args:
            rect (pygame.Rect): Area at which the grid manager will work.
            tile_size (int): Size of each tile.

        Returns:
            None
        """
        self.rect = rect
        self.size = rect.size
        self.tile_size = tile_size
        self._control_block = ControlBlock(tile_size, self.rect)
        self.surf = pygame.Surface(rect.size, pygame.SRCALPHA)

    def update(self, event_builder: EventBuilder) -> None:
        """Updates the GridManager.

        Args:
            event_builder (EventBuilder): A reference to the game's
            sole `EventBuilder` instance

        Returns:
            None
        """
        self._control_block.update(event_builder.mouse_pos)

    def draw(self, screen: pygame.Surface) -> None:
        """Draws the Grid Element.

        Args:
            screen (pygame.Surface): Surface to draw on.

        Returns:
            None
        """
        self.surf.fill("black")
        self._control_block.draw(self.surf)
        screen.blit(self.surf, self.rect)
        for col in range(self.size[0] // self.tile_size):
            coord = col * self.tile_size
            pygame.draw.line(
                screen,
                "white",
                self.rect.topleft + pygame.Vector2(coord, 0),
                self.rect.topleft + pygame.Vector2(coord, self.rect.height),
            )
        for row in range(self.size[1] // self.tile_size):
            coord = row * self.tile_size
            pygame.draw.line(
                screen,
                "white",
                self.rect.topleft + pygame.Vector2(0, coord),
                self.rect.topleft + pygame.Vector2(self.rect.width, coord),
            )
        pygame.draw.rect(screen, "white", self.rect, width=1)
