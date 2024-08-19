from __future__ import annotations
from abc import ABC, abstractmethod


class Accum:
    def __init__(self, valor_inicial):
        self._valor = valor_inicial

    def adiciona(self, valor):
        self._valor += valor


class Component(ABC):
    """Interface abstrata do componente"""

    @abstractmethod
    def execute(self) -> str: ...


class ConcreteComponent(Component):
    """Componente concreto"""

    def __init__(self, a: Accum, valor):
        self._a = a
        self._valor = valor

    def execute(self):
        self._a.adiciona(self._valor)


class BaseDecorator(Component):
    def __init__(self, c: Component, a: Accum, valor):
        self._wrappee = c
        self._a = a
        self._valor = valor

    @property
    def component(self) -> Component:
        return self._wrappee

    @abstractmethod
    def execute(self) -> str: ...


class ConcreteDecoratorA(BaseDecorator):
    def execute(self):
        self._a.adiciona(2 * self._valor)
        return self.component.execute()


class ConcreteDecoratorB(BaseDecorator):
    def execute(self):
        self._a.adiciona(self._valor)
        return self.component.execute()


def client_code(c: Component, a: Accum):
    c.execute()
    print(f"Resultado: {a._valor}")


if __name__ == "__main__":
    accum = Accum(0)
    a = ConcreteComponent(accum, 3)
    b = ConcreteDecoratorA(a, accum, 3)
    c = ConcreteDecoratorB(b, accum, 10)
    client_code(c, accum)
