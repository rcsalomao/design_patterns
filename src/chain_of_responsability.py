from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler: ...

    @abstractmethod
    def handle(self, request): ...


class BaseHandler(Handler):
    """
    The default chaining behavior can be
    implemented inside a base handler class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us
        # link handlers in a convenient way like this:
        # ch1.set_next(ch2).set_next(ch3)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        else:
            return None


"""
All Concrete Handlers either handle a request
or pass it to the next handler in the chain.
"""


class ConcreteHandler1(BaseHandler):
    def handle(self, request: Any) -> str:
        if request == "valor_1":
            return f"Resultado de ConcreteHandler1: {request}"
        else:
            return super().handle(request)


class ConcreteHandler2(BaseHandler):
    def handle(self, request: Any) -> str:
        if request == "valor_2":
            return f"Resultado de ConcreteHandler2: {request}"
        else:
            return super().handle(request)


class ConcreteHandler3(BaseHandler):
    def handle(self, request: Any) -> str:
        if request == "valor_3":
            return f"Resultado de ConcreteHandler3: {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler.
    In most cases, it is not even aware that the handler is part of a chain.
    """

    for valor in ["valor_2", "valor_1", "valor_3"]:
        print(f"Client: Qual vai ser o handler que vai ser ativado com o {valor}?")
        result = handler.handle(valor)
        if result:
            print(f"  {result}")
        else:
            print(f"  {valor} foi ignorado.")


if __name__ == "__main__":
    ch1 = ConcreteHandler1()
    ch2 = ConcreteHandler2()
    ch3 = ConcreteHandler3()

    ch1.set_next(ch2).set_next(ch3)

    # The client should be able to send a request to any handler,
    # not just the first one in the chain.

    print("Chain: ch1 > ch2 > ch3")
    client_code(ch1)

    print()

    print("Subchain: ch2 > ch3")
    client_code(ch2)
