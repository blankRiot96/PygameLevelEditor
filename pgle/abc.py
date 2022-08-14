from abc import ABC

class Singleton(ABC):
    _inst = None

    def __new__(cls):
        if cls._inst is None:
            self = object.__new__(cls)
            cls._inst = self
        return cls._inst

    def __init__(self):
        if self._inst:
            return



