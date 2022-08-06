"""
This file is a part of the 'PygameLevelEditor' source code.
The source code is distributed under the MIT license.

A file containing all the generic types used
throughout the code base.
"""


import enum
from typing import Sequence

import pygame


class Controls(enum.Enum):
    SINGLE = enum.auto()
    HOLD = enum.auto()


PygameEvent = int
ControlName = str
Control = dict[ControlName, list[PygameEvent]]
ControlsType = dict[Controls, Control]

Pos = tuple | list | Sequence | pygame.Vector2
