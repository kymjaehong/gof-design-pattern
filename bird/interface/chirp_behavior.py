from abc import ABC, abstractmethod


class ChirpBehavior(ABC):
    @abstractmethod
    def chirp(self):
        pass
