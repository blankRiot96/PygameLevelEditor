import enum


class Controls(enum.Enum):
    SINGLE = enum.auto()
    HOLD = enum.auto()


PygameEvent = int
ControlName = str
Control = dict[ControlName, list[PygameEvent]]
ControlsType = dict[Controls, Control]
