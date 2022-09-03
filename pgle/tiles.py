import pygame
from pgle._types import Pos


class Tile:
    """Flexible Tile class for the Tiled Layer"""

    REGISTERED_SURFS = {}

    def __init__(self, image: pygame.Surface, image_path: str, pos: Pos, tile_type: str, tile_id: int) -> None:
        self.image = image
        self.tile_type = tile_type
        self.image_path = image_path
        self.pos = pos
        self.id_ = tile_id

    @classmethod
    def from_json(cls, tile_dict: dict):
        if tile_dict["type"] not in cls.REGISTERED_SURFS:
            cls.REGISTERED_SURFS[tile_dict["type"]] = pygame.image.load(tile_dict["image"])
        return Tile(
            cls.REGISTERED_SURFS[tile_dict["type"]],
            tile_dict["image"],
            tile_dict["pos"],
            tile_dict["type"],
            tile_dict["id"]
        )

    def draw(self, surf):
        surf.blit(self.image, self.pos)
