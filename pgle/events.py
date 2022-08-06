"""
This file is a part of the 'PygameLevelEditor' source code.
The source code is distributed under the MIT license.
"""

import pygame
from loguru import logger

from pgle._types import Controls, ControlsType


class EventBuilder:
    """
    An event builder to build all events when required
    and is easily accessible across the code base.
    There is only one event builder object meant to be defined,
    and its references are meant to be passed down along the
    abstraction hierarchy.
    Example: Game -> EditorState -> GridManager
    """

    def __init__(self) -> None:
        self.events = []
        self.mouse_pos = []
        self.key_pressed = []
        self.mouse_press = ()

    def is_key_held(self, key: int) -> bool:
        """Checks if given key is being held.

        Args:
            key: The key to be checked if it is being held.

        Returns:
            If the key is being held. True if it is, False if otherwise.
        """
        return self.key_pressed[key]

    def is_key_pressed(self, key: int) -> bool:
        """Checks if given key has been pressed once.

        Args:
            key: The key to be checked if it is has been pressed.

        Returns:
            If the key has been held. True only after it has been released once,
            False otherwise.
        """
        for event in self.events:
            if event.type == key:
                return True

            if event.type == pygame.KEYDOWN:
                if event.key == key:
                    return True
        return False

    def build(self):
        """Builds all the required events."""
        self.events = pygame.event.get()
        self.mouse_pos = pygame.mouse.get_pos()
        self.key_pressed = pygame.key.get_pressed()
        self.mouse_press = pygame.mouse.get_pressed()


class ControlScheme:
    """Handles your custom control scheme.

    The controls dictionary goes like so,
    {
        Controls.SINGLE: ControlType,
        Controls.HOLD: ControlType
    }

    The `Controls.SINGLE` is mapped to a `ControlType`,
    which indicates that every control listed there is on
    a single click/press.

    The `Controls.HOLD` is mapped to a `ControlType`,
    which indicates that every control listed there is
    meant to activate for as long as they are being held.
    They deactivate when released.

    `ControlType` looks like so,
    {
        "right": [pygame.K_d, pygame.K_RIGHT],
        "left": [pygame.K_a, pygame.K_LEFT]
    }
    This specifies the schema through which the controls will be specified.
    So, "right" is triggered/activated when a `pygame.K_d` or `pygame.K_RIGHT`
    event is triggered.

    Attributes:
        controls (dict): A dictionary containing
                         information pertaining the controls.
    """

    def __init__(self, event_builder: EventBuilder, controls: ControlsType) -> None:
        """Constructor of the ControlScheme class.

        Args:
            event_builder (EventBuilder): A reference to the game's
            sole `EventBuilder` instance, which has all the required
            events to be used to check if certain controls are being triggered.
            controls (ControlsType): A dictionary containing the information
            pertaining to the control scheme.

        Returns:
            None
        """
        self._event_builder = event_builder
        self.controls = controls

    def get_controls(self) -> list[str]:
        """Gets all the triggered controls.

        Returns:
            A list of all the controls triggered,
            Example: ["right", "up"]
        """
        controls = []
        single_controls = self.controls[Controls.SINGLE]
        hold_controls = self.controls[Controls.HOLD]
        for control, events in single_controls.items():
            if any(self._event_builder.is_key_pressed(key) for key in events):
                controls.append(control)

        for control, events in hold_controls.items():
            if any(self._event_builder.is_key_held(key) for key in events):
                controls.append(control)

        return controls
