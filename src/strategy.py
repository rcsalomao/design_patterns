from __future__ import annotations
from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, data): ...


class ConcreteStrategy1(Strategy):
    def execute(self, data):
        return f"Resultado da estratégia 1: {data}"


class ConcreteStrategy2(Strategy):
    def execute(self, data):
        return f"Resultado da estratégia 2: {data}"


class Context:
    def __init__(self):
        self._strategy = None

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_something(self, data):
        if self._strategy is not None:
            print(self._strategy.execute(data))
        else:
            raise Exception("Estratégia de execução não informada")


def client_code():
    str1 = ConcreteStrategy1()
    str2 = ConcreteStrategy2()
    context = Context()
    context.set_strategy(str1)
    context.do_something("argumento 1")
    context.set_strategy(str2)
    context.do_something("argumento 2")


if __name__ == "__main__":
    client_code()
