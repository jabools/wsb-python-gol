from abc import ABC, abstractmethod


class ModelBase(ABC):
    def __init__(self):
        super().__init__()
        self._observers = dict()

    def add_observer(self, obs):
        if obs.name not in self._observers:
            self._observers[obs.name] = obs

    def remove_observer(self, name):
        if name in self._observers:
            del self._observers[name]

    @abstractmethod
    def modify(self, *args, **kwargs):
        pass

    @abstractmethod
    def notify(self):
        pass
