from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from copy import deepcopy
from random import random


class DataModel(object):
    def __init__(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def set_data(self, data) -> None:
        self._data = data


class EventHandler(ABC):
    @abstractmethod
    def execute(self, data_model: DataModel, events: List[EventHandler]):
        pass


class SimpleEventHandler(EventHandler):
    def __init__(self):
        pass

    def execute(self, data_model: DataModel, events: List[EventHandler]):
        data_model.set_data(data_model.get_data() + random())
        num = data_model.get_data()
        if num < 10:
            print(num)
            events.append(SimpleEventHandler())


class Context(object):
    def __init__(
        self, data_model: DataModel, event_handlers: List[EventHandler] = None
    ):
        self._data_model = data_model
        self._event_queue = [] if event_handlers is None else deepcopy(event_handlers)

    def run(self) -> None:
        while self._event_queue:
            event_handler = self._event_queue.pop(0)
            event_handler.execute(self._data_model, self._event_queue)

    def get_data_model(self) -> DataModel:
        return self._data_model


c = Context(DataModel(5), [SimpleEventHandler()])
c.run()
dm = c.get_data_model()
print(dm.get_data())
