from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_product(self): ...


class ConcreteFactory1(AbstractFactory):
    def create_product(self) -> Product:
        return ConcreteProduct1()


class ConcreteFactory2(AbstractFactory):
    def create_product(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    @abstractmethod
    def operation(self): ...


class ConcreteProduct1(Product):
    def operation(self):
        return "Result of the ConcreteProduct1"


class ConcreteProduct2(Product):
    def operation(self):
        return "Result of the ConcreteProduct2"


def client_code(factory: AbstractFactory) -> None:
    product: Product = factory.create_product()
    print(
        f"Client: I'm not aware of the factory's class, but it still works.\n"
        f"{product.operation()}"
    )


if __name__ == "__main__":
    print("Client code launched with the ConcreteFactory1.")
    client_code(ConcreteFactory1())
    print()
    print("Client code launched with the ConcreteFactory2.")
    client_code(ConcreteFactory2())
