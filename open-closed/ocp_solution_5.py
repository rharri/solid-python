# ocp_solution_5.py
# !/usr/bin/env python3
"""The fifth solution.

Use the strategy design pattern and functions.

"Strategy is a behavioral design pattern that lets you define a family of
algorithms, put each of them into a separate class, and make their objects
interchangeable." (https://refactoring.guru/design-patterns/strategy)
"""

from typing import Callable


def parse_phone_number(value: str) -> str:
    # FIXME: Parse value and ensure valid phone number
    pass


def parse_email_address(value: str) -> str:
    # FIXME: parse x and ensure valid email address
    pass


# Type alias
ContactMethod = Callable[["Customer", str], None]


class Customer:
    """Represents a customer.

    Public attributes:
    - phone_number
    - email_address
    - preferred_contact_method
    """

    def __init__(
        self,
        phone_number: str,
        email_address: str,
        preferred_contact_method: ContactMethod,
    ) -> None:
        self.phone_number = parse_phone_number(phone_number)
        self.email_address = parse_email_address(email_address)
        self.preferred_contact_method = preferred_contact_method


def make_call(customer: Customer, message: str) -> None:
    """Send the message via telephone.

    Args:
        customer: The intended recipient of the message.
        message: The message to send.
    """
    phone_number: str = customer.phone_number
    print(f"phone call made to {phone_number} with message: '{message}'")


def send_sms(customer: Customer, message: str) -> None:
    """Send the message via SMS.

    Args:
        customer: The intended recipient of the message.
        message: Message to send.
    """
    phone_number: str = customer.phone_number
    print(f"sms sent to {phone_number} with message: '{message}'")


def send_email(customer: Customer, message: str) -> None:
    """Sends the message via email.

    Args:
        customer: The intended recipient of the message.
        message: Message to send.
    """
    email_address: str = customer.email_address
    print(f"email sent to {email_address} with subject: '{message}'")


# This function is now closed for modification, but open to extension. A new
# sender can be implemented as a function.
def contact_customer(customer: Customer, message: str) -> None:
    """Send a message to the customer based on their preferred contact method.

    Args:
        customer: The customer to contact.
        message: The message for the customer.
    """
    customer.preferred_contact_method(customer, message)


if __name__ == "__main__":
    customers = (
        Customer("555-7302", "bob@solid.com", send_email),
        Customer("555-7303", "raj@solid.com", send_sms),
        Customer("555-7304", "sofia@solid.com", make_call),
    )

    for customer in customers:
        contact_customer(customer, "Bill Payment Due")
