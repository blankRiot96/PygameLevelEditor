import pygame
from pgle._types import Control, Controls
from loguru import logger


class EventBuilder:
    def __init__(self) -> None:
        self.events = []
        self.mouse_pos = []
        self.key_pressed = []
        self.mouse_press = ()

    def is_key_held(self, key: int) -> bool:
        return self.key_pressed[key]

    def is_key_pressed(self, key: int) -> bool:
        for event in self.events:
            if event.type == key:
                return True
            
            if event.type == pygame.KEYDOWN:
                if event.key == key:
                    return True
        return False

    def build(self):
        self.events = pygame.event.get()
        self.mouse_pos = pygame.mouse.get_pos()
        self.key_pressed = pygame.key.get_pressed()
        self.mouse_press = pygame.mouse.get_pressed()


class ControlScheme:
    def __init__(self, event_builder: EventBuilder, controls: Control) -> None:
        self.event_builder = event_builder
        self.controls = controls

    def get_controls(self) -> list[str]:
        controls = []
        single_controls = self.controls[Controls.SINGLE]
        hold_controls = self.controls[Controls.HOLD]
        for control, events in single_controls.items():
            if any(self.event_builder.is_key_pressed(key) for key in events):
                controls.append(control)

        for control, events in hold_controls.items():
            if any(self.event_builder.is_key_held(key) for key in events):
                controls.append(control)

        return controls
