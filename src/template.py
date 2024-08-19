from __future__ import annotations
from abc import ABC, abstractmethod


class Template(ABC):
    def template_method(self):
        a = 0
        a += self.step_1()
        if self.step_2():
            a *= 2
        else:
            a *= 3
        return a

    def step_1(self):
        return 0

    def step_2(self):
        return True


class ConcreteClass1(Template):
    def step_1(self):
        return 10


class ConcreteClass2(Template):
    def step_1(self):
        return 5

    def step_2(self):
        return False


def client_code():
    """docstring for client_code"""
    c = ConcreteClass1()
    o = c.template_method()
    print(o)

    c = ConcreteClass2()
    o = c.template_method()
    print(o)


if __name__ == "__main__":
    client_code()
