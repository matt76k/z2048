from abc import ABC, abstractmethod
from typing import Tuple

import random
import pygame

class Controller(ABC):
    @abstractmethod
    def update(self, board:list[list[int]], score: int) -> str:
        return random.choice(["left", "right", "up", "down"])


class Human(Controller):
    def __init__(self) -> None:
        super().__init__()

    def update(self, board:list[list[int]], score: int) -> str:
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_LEFT]:
            return "left"
        if pressedKeys[pygame.K_RIGHT]: 
            return "right"
        if pressedKeys[pygame.K_UP]:
            return "up"
        if pressedKeys[pygame.K_DOWN]:
            return "down"
        return ""