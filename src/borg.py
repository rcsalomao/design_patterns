# from __future__ import annotations
# from abc import ABC, abstractmethod


class Borg(object):
    _shared_state = {}

    def __new__(cls):
        inst = super().__new__(cls)
        inst.__dict__ = cls._shared_state
        return inst


class Foo(Borg):
    _shared_state = {}


def client_code():
    b0 = Borg()
    b1 = Borg()
    print(b0 is b1)
    b0.a = 3
    print(b0.a, b1.a)

    f0 = Foo()
    f1 = Foo()
    f0.a = 4
    print(b0.a, b1.a, f0.a, f1.a)


if __name__ == "__main__":
    client_code()
