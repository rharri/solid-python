# liskov_substitution.py
# !/usr/bin/env python3
"""A demonstration of the Liskov Substitution Principle

- Clients can use a subclass of their choice without changes or unexpected
behaviour

If S is a subtype of T, then objects of type T may be replaced with objects
of type S, without breaking the program

LSP rules:
- "Preconditions cannot be strengthened in a subtype"
- "Postconditions cannot be weakened in a subtype"
- "Invariants of the supertype must be preserved in a subtype"
- "There must be contravariance of the method arguments in the subtype"
- "There must be covariance of the return types in the subtype"
- "No new exceptions can be thrown by the subype unless they are part of the
existing exception hierarchy"

Covariance and Contravariance:
- " ... covariance is a relationship where subtypes go with each other, and
contravariance is a relationship where subtypes go against each other."

class A:
    def spam(t: A) -> A:
        pass

class B(A):
    def spam(t: object) -> B:
        pass

Contravariance:
- In class B, spam should not accept an argument more specialized than A

Covariance:
- In class B, spam should not return a type more general than A

Source: Adaptive Code, Second Edition (Microsoft Press, 2017)
"""

import json
from typing import Iterator, MutableMapping


class StrictMapping(MutableMapping):
    """A mapping object that maps keys to values.

    Keys and values must not be None.
    """

    def __init__(self) -> None:
        self.mapping: dict = {}

    def __getitem__(self, key: object) -> object:
        return self.mapping.get(key)

    def __setitem__(self, key: object, item: object) -> None:
        # Violates LSP since these preconditions are stronger than those
        # implied by MutableMapping
        if key is None:
            raise ValueError("Key cannot be None.")
        if item is None:
            raise ValueError("Item cannot be None.")
        self.mapping[key] = item

    def __delitem__(self, key: object) -> None:
        del self.mapping[key]

    def __iter__(self) -> Iterator:
        return iter(self.mapping)

    def __len__(self) -> int:
        return len(self.mapping)


# Create an instance of a built-in dict
std_dict: dict = {}
std_dict["key"] = "value"

assert isinstance(std_dict, MutableMapping)

# Create an instance of a StrictMapping
strict_mapping: StrictMapping = StrictMapping()
strict_mapping["key"] = "value"

assert isinstance(strict_mapping, MutableMapping)


# We just want to work with a MutableMapping, we do not care about a
# specific one
def replace_values(mapping: MutableMapping, json_doc: str) -> None:
    """Replace the values of mapping with the values of the provided JSON
    document.

    Args:
        mapping: A mutable mapping.
        json_string: String representation of the JSON document.
    """
    obj: dict[str, str] = json.loads(json_doc)
    for key, value in obj.items():
        print(f"... replacing key={key} with value={value}")
        mapping[key] = value


replace_values(std_dict, '{"key": null}')  # Works!
replace_values(strict_mapping, '{"key": null}')  # Oops.. ValueError


# In this case StrictMapping is not substitutable for a MutableMapping

# Possible solutions:
# 1. StrictMapping should not subclass MutableMapping
# 2. Handle ValueError in replace_values
# 3. Precondition in replace_values that the mapping can set a None value
# 4. Do not allow None value to be set; replace with placeholder value
