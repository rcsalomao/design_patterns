from __future__ import annotations
from abc import ABC, abstractmethod


class Element(ABC):
    @abstractmethod
    def accept(self, v: Visitor): ...


class ElementA(ABC):
    def accept(self, v: Visitor):
        v.visit_A(self)

    def feature_A(self):
        return 4


class ElementB(ABC):
    def accept(self, v: Visitor):
        v.visit_B(self)

    def feature_B(self):
        return 2


class Visitor(ABC):
    @abstractmethod
    def visit_A(self, e: Element): ...
    @abstractmethod
    def visit_B(self, e: Element): ...


class ConcreteVisitor1(Visitor):
    def visit_A(self, e: Element):
        print(e.feature_A())

    def visit_B(self, e: Element):
        print(e.__str__())
        print(e.feature_B())


def client_code():
    elem = ElementB()
    visitor = ConcreteVisitor1()
    elem.accept(visitor)


if __name__ == "__main__":
    client_code()
