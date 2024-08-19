from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List
from math import floor


class Subscriber(ABC):
    @abstractmethod
    def update(self, publisher: Publisher): ...


class ConcreteSubscriber1(Subscriber):
    def update(self, publisher: Publisher):
        n = randrange(1, 11)
        if n > 2:
            publisher._main_state = floor(publisher._main_state / 2)
        else:
            publisher._main_state *= 2


class ConcreteSubscriber2(Subscriber):
    def update(self, publisher: Publisher):
        n = randrange(1, 11)
        if n > 8:
            publisher._main_state = floor(publisher._main_state / 2)
        else:
            publisher._main_state *= 2


class Publisher:
    def __init__(self, main_state: int):
        self._main_state = main_state
        self._subscribers: List[Subscriber] = []

    def subscribe(self, s: Subscriber):
        test = s in self._subscribers
        if not test:
            self._subscribers.append(s)

    def unsubscribe(self, s: Subscriber):
        test = s in self._subscribers
        if test:
            self._subscribers.remove(s)

    def notify_subscribers(self):
        for s in self._subscribers:
            s.update(self)


def client_code():
    pub = Publisher(5)
    sub1 = ConcreteSubscriber1()
    sub2 = ConcreteSubscriber2()
    pub.subscribe(sub1)
    pub.subscribe(sub2)
    print(pub._main_state)
    pub.notify_subscribers()
    print(pub._main_state)
    pub.unsubscribe(sub1)
    pub.notify_subscribers()
    print(pub._main_state)


if __name__ == "__main__":
    client_code()
