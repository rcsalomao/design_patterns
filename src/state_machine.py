from __future__ import annotations
from enum import Enum, auto, unique
from random import random


@unique
class EventMessage(Enum):
    POSTINITIAL = auto()
    SUCCESS = auto()
    ERROR = auto()
    RESET = auto()


@unique
class State(Enum):
    INITIAL = auto()
    POSTINITIAL = auto()
    SUCCESS = auto()
    ERROR = auto()


class StateManager:
    @staticmethod
    def get_next_state(event: EventMessage, state: State):
        match state:
            case State.INITIAL:
                match event:
                    case EventMessage.POSTINITIAL:
                        return State.POSTINITIAL
                    case _:
                        return state
            case State.POSTINITIAL:
                match event:
                    case EventMessage.SUCCESS:
                        return State.SUCCESS
                    case EventMessage.ERROR:
                        return State.ERROR
                    case _:
                        return state
            case State.SUCCESS:
                match event:
                    case EventMessage.RESET:
                        return State.INITIAL
                    case _:
                        return state
            case State.ERROR:
                match event:
                    case EventMessage.RESET:
                        return State.INITIAL
                    case _:
                        return state

    @staticmethod
    def execute(subject: Subject):
        state = subject._state
        match state:
            case State.INITIAL:
                print("Initial state")
                subject.change_state(EventMessage.POSTINITIAL)
            case State.POSTINITIAL:
                print("Post initial state")
            case State.SUCCESS:
                print("Success state")
            case State.ERROR:
                print("Error state")


class Subject(object):
    def __init__(self, state: State = None):
        self._state: State = State.INITIAL if state is None else state

    def change_state(self, event: EventMessage):
        self._state = StateManager.get_next_state(event, self._state)

    def execute(self):
        StateManager.execute(self)

    def do_stuff_that_may_change_state(self):
        r = random()
        if r < 0.5:
            self.change_state(EventMessage.SUCCESS)
        else:
            self.change_state(EventMessage.ERROR)

    def reset(self):
        self.change_state(EventMessage.RESET)


a = Subject()
print(a._state)
a.execute()
print(a._state)
a.do_stuff_that_may_change_state()
print(a._state)
a.execute()
print(a._state)
a.reset()
print(a._state)
a.execute()
print(a._state)
