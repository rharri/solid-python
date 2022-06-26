# contravariance_aside.py
# !/usr/bin/env python3

# Run mypy to see type errors


class A:
    def spam(self, t: "A") -> None:
        # Because this method accepts A as an argument
        # All subtypes that override this method will be constrained
        # by this argument type
        print("Spam from A.")


class B(A):
    def spam(self, t: "B") -> None:  # LSP violation: No contravariance
        # This method may have to accept an A at some point
        # This method should accept at least A or a supertype of A
        print("Spam from B.")
        t.eggs()

    def eggs(self):
        print("Eggs from B.")


# We want to work with an A and thanks to polymorphism we may in fact be
# working with a B, however we do not care about the implementation, only
# the interface (i.e. we can call spam with an argument of type A)
def use_a(a: A) -> None:
    some_a = A()
    a.spam(some_a)  # 'a' may be a subtype of A implicitly


a = A()
use_a(a)

b = B()
use_a(b)  # <--- Polymorphism at work!
