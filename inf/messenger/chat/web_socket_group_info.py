
from abc import ABC, abstractmethod

class GroupInfo(ABC):
    @abstractmethod
    def get_name(self):
        pass