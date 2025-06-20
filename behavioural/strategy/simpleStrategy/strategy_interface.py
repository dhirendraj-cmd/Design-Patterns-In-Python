#  creating startegy interface using abstract module in python
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def operations(self, a, b):
        pass



