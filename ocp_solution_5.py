# ocp_solution_5.py
# !/usr/bin/env python3
"""The fifth solution.

Use the strategy design pattern and functions.

"Strategy is a behavioral design pattern that lets you define a family of
algorithms, put each of them into a separate class, and make their objects
interchangeable." (https://refactoring.guru/design-patterns/strategy)
"""

from dataclasses import dataclass
from typing import Callable


@dataclass
class Customer:
    """Represents a customer.

    Public attributes:
    - phone_number
    - email_address
    - preferred_contact_method
    """

    phone_number: str
    email_address: str
    preferred_contact_method: Callable[["Customer", str], None]


def makeCall(customer: Customer, message: str) -> None:
    """Send the message via telephone.

    Args:
        customer: The intended recipient of the message.
        message: The message to send.
    """
    phone_number: str = customer.phone_number
    print(f"phone call made to {phone_number} with message: '{message}'")


def sendSMS(customer: Customer, message: str) -> None:
    """Send the message via SMS.

    Args:
        customer: The intended recipient of the message.
        message: Message to send.
    """
    phone_number: str = customer.phone_number
    print(f"sms sent to {phone_number} with message: '{message}'")


def sendEmail(customer: Customer, message: str) -> None:
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
    contact_method = customer.preferred_contact_method
    contact_method(customer, message)


if __name__ == "__main__":
    customers = (
        Customer("555-7302", "bob@solid.com", sendEmail),
        Customer("555-7303", "raj@solid.com", sendSMS),
        Customer("555-7304", "sofia@solid.com", makeCall),
    )

    for customer in customers:
        contact_customer(customer, "Bill Payment Due")
