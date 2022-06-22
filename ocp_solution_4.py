# ocp_solution_3.py
# !/usr/bin/env python3
"""The fourth solution."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type


class Sender(ABC):
    def __init__(self, customer: "Customer") -> None:
        self.customer = customer

    @classmethod
    def __subclasshook__(cls, sub):
        return hasattr(sub, "sendMessage") and callable(sub.sendMessage)

    @abstractmethod
    def sendMessage(self, message: str) -> None:
        raise NotImplementedError


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
    preferred_contact_method: Type[Sender]  # Reference to the class


class Phone(Sender):
    """Represents a phone service."""

    def __init__(self, customer: Customer) -> None:
        """Initializes an instance of Phone.

        Args:
            customer: Customer to call.
        """
        self.customer = customer

    def sendMessage(self, message: str) -> None:
        """Sends the message.

        Args:
            message: The message to send.
        """
        phone_number = self.customer.phone_number
        print(f"phone call made to {phone_number} with message: '{message}'")


class SMS(Sender):
    """Represents an SMS sender."""

    def __init__(self, customer: Customer) -> None:
        """Initializes an instance of SMS.

        Args:
            customer: Customer to message.
        """
        self.customer = customer

    def sendMessage(self, message: str) -> None:
        """Sends the message.

        Args:
            message: Message to send.
        """
        phone_number = self.customer.phone_number
        print(f"sms sent to {phone_number} with message: '{message}'")


class Email(Sender):
    """Represents an email sender."""

    def __init__(self, customer: Customer) -> None:
        """Initializes an instance of Email.

        Args:
            customer: Customer to email.
        """
        self.customer = customer

    def sendMessage(self, message: str) -> None:
        """Sends the message.

        Args:
            message: Message to send.
        """
        email_address = self.customer.email_address
        print(f"email sent to {email_address} with subject: '{message}'")


# This function is now closed for modification, but open to extension. A new
# sender can be implemented as a class that inherits from Sender.
def contact_customer(customer: Customer, message: str) -> None:
    """Send a message to the customer based on their preferred contact method.

    Args:
        customer: The customer to contact
        message: The message for the customer.
    """
    contact_method: Type[Sender] = customer.preferred_contact_method
    contact_method(customer).sendMessage(message)


if __name__ == "__main__":
    customers = (
        Customer("555-7302", "bob@solid.com", Email),
        Customer("555-7303", "raj@solid.com", SMS),
        Customer("555-7304", "sofia@solid.com", Phone),
    )

    for customer in customers:
        contact_customer(customer, "Bill Payment Due")
