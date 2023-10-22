from abc import ABC, abstractmethod
import json

class IStrategy(ABC):

    @abstractmethod
    def searchFor(self, a, b):
        pass