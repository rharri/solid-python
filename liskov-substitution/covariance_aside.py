# covariance_aside.py
# !/usr/bin/env python3

# Run mypy to see type errors


class A:
    def spam(self, t: "A") -> "A":
        # Returning A constrains all subtypes to return A or a subtype of A
        print("Spam from A.")
        return A()


class B(A):
    def spam(self, t: "A") -> object:  # LSP violation: No covariance
        # If the caller is working A's interface, they expect to get back an A
        # or a subtype of A
        print("Spam from B.")
        return B()


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
