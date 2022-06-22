# ocp_solution_2.py
# !/usr/bin/env python3
"""The second solution.

Use the strategy design pattern and a class.

"Strategy is a behavioral design pattern that lets you define a family of
algorithms, put each of them into a separate class, and make their objects
interchangeable." (https://refactoring.guru/design-patterns/strategy)
"""

from dataclasses import dataclass
from enum import Enum
from types import MappingProxyType


class ContactMethod(Enum):
    PHONE = 1
    SMS = 2
    EMAIL = 3


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
    preferred_contact_method: ContactMethod


class Phone:
    """Represents a phone service."""

    def __init__(self, customer: Customer) -> None:
        """Initializes an instance of Phone.

        Args:
            customer: Customer to call.
        """
        self.customer = customer

    @property
    def type(self):
        """The type of this sender."""
        return ContactMethod.EMAIL

    def sendMessage(self, message: str) -> None:
        """Sends the message.

        Args:
            message: The message to send.
        """
        phone_number = self.customer.phone_number
        print(f"phone call made to {phone_number} with message: '{message}'")


class SMS:
    """Represents an SMS sender."""

    def __init__(self, customer: Customer) -> None:
        """Initializes an instance of SMS.

        Args:
            customer: Customer to message.
        """
        self.customer = customer

    @property
    def type(self):
        """The type of this sender."""
        return ContactMethod.SMS

    def sendMessage(self, message: str) -> None:
        """Sends the message.

        Args:
            message: Message to send.
        """
        phone_number = self.customer.phone_number
        print(f"sms sent to {phone_number} with message: '{message}'")


class Email:
    """Represents an email sender."""

    def __init__(self, customer: Customer) -> None:
        """Initializes an instance of Email.

        Args:
            customer: Customer to email.
        """
        self.customer = customer

    @property
    def type(self):
        """The type of this sender."""
        return ContactMethod.EMAIL

    def sendMessage(self, message: str) -> None:
        """Sends the message.

        Args:
            message: Message to send.
        """
        email_address = self.customer.email_address
        print(f"email sent to {email_address} with subject: '{message}'")


# This essentially a dictionary - Is this really an improvement?
class Sender:
    """Represents a sender."""

    # PEP 416 – Add a frozendict builtin type
    _available_senders = MappingProxyType(
        {
            ContactMethod.PHONE: Phone,
            ContactMethod.SMS: SMS,
            ContactMethod.EMAIL: Email,
        }
    )

    def __init__(self, contact_method: ContactMethod) -> None:
        """Initializes an instance of Sender."""
        self.contact_method = contact_method

    def getSender(self):
        """Returns a sender based on the contact method."""
        return Sender._available_senders[self.contact_method]


# This function is now closed for modification, but open to extension. A new
# sender can be added to the Sender class.
def contact_customer(customer: Customer, message: str) -> None:
    """Send a message to the customer based on their preferred contact method.

    Args:
        customer: The customer to contact.
        message: The message for the customer.
    """
    # duck type polymorphism
    sender = Sender(customer.preferred_contact_method).getSender()
    sender(customer).sendMessage(message)


if __name__ == "__main__":
    customers = (
        Customer("555-7302", "bob@solid.com", ContactMethod.EMAIL),
        Customer("555-7303", "raj@solid.com", ContactMethod.SMS),
        Customer("555-7304", "sofia@solid.com", ContactMethod.PHONE),
    )

    for customer in customers:
        contact_customer(customer, "Bill Payment Due")
