# abc_aside.py
# !/usr/bin/env python3
from abc import ABC, abstractmethod


class Menu(ABC):
    @abstractmethod
    def add_spam(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def chef_special(self) -> None:
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, sub):
        """Required to support duck typing."""
        return (
            hasattr(sub, "add_spam")
            and callable(sub.add_spam)
            and hasattr(sub, "chef_special")
            and callable(sub.chef_special)
        ) or NotImplemented  # Not True or False


class LunchMenu(Menu):
    def add_spam(self) -> None:
        pass

    def chef_special(self) -> None:
        pass


# Possible because of inheritance of Menu class
assert LunchMenu.__mro__ == (LunchMenu, Menu, ABC, object)  # True
assert isinstance(LunchMenu(), Menu)  # True
assert issubclass(LunchMenu, Menu)  # True


class TakeoutMenu:
    def add_spam(self) -> None:
        pass

    def chef_special(self) -> None:
        pass


# Possible because of __subclasshook__()
assert TakeoutMenu.__mro__ == (TakeoutMenu, object)  # True, no menu or ABC
assert isinstance(TakeoutMenu(), Menu)  # True
assert issubclass(TakeoutMenu, Menu)  # True


@Menu.register
class DinnerMenu:
    def add_spam(self) -> None:
        pass


# Possible because of 'Or NotImplemented' condition in __subclasshook__()
assert DinnerMenu.__mro__ == (DinnerMenu, object)  # True, no menu or ABC
assert isinstance(DinnerMenu(), Menu)  # True, no chef_special
assert issubclass(DinnerMenu, Menu)  # True, no chef_special

# Inheritance strictness in Python - from strict to less strict
# Class-based inheritance
# ABC
# ABC w/ __subclasshook__()
# ABC w/ register + __subclasshook__()
# Duck typing

# Sources:
# https://jarombek.com/blog/dec-15-2018-python-protocols-abcs
# https://jellis18.github.io/post/2022-01-11-abc-vs-protocol/
# http://leanpub.com/python-master (Robert Smallshire, Austin Bingham and Sixty North) # noqa
# https://peps.python.org/pep-3119/
