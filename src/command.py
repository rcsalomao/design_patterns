from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self): ...


class Command1(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self):
        print(f"Command1: See, I can do simple things like printing ({self._payload})")


class Command2(Command):
    """
    However, some commands can delegate more
    complex operations to other objects, called "receivers."
    """

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """
        Complex commands can accept one or several receiver objects
        along with any context data via the constructor.
        """
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self):
        """
        Commands can delegate to any methods of a receiver.
        """
        print("Command2: Complex stuff should be done by a receiver object")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    """
    The Receiver classes contain some important business logic.
    They know how to perform all kinds of operations,
    associated with carrying out a request.
    In fact, any class may serve as a Receiver.
    """

    def do_something(self, a: str) -> None:
        print(f"    Receiver: Working on ({a}).")

    def do_something_else(self, b: str) -> None:
        print(f"    Receiver: Also working on ({b}).")


class Invoker:
    """
    The Invoker is associated with one or several commands.
    It sends a request to the command.
    """

    _on_start = None
    _on_finish = None

    """
    Initialize commands.
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        The Invoker does not depend on concrete command or receiver classes.
        The Invoker passes a request to a receiver indirectly,
        by executing a command.
        """

        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")
        print("    Blep c:")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


def client_code():
    invoker = Invoker()
    invoker.set_on_start(Command1("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(Command2(receiver, "Send email", "Save report"))
    invoker.do_something_important()


if __name__ == "__main__":
    """
    The client code can parameterize an invoker with any commands.
    """
    client_code()
