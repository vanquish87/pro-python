from abc import ABC, abstractmethod


class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


# Interface Segregation
# Make interfaces (parent abstract classes) more specific, rather than generic.
# e.g. Create more interfaces (classes) if needed and/or provide objects to constructors.
# using composition ie, creating a whole new Class
class SMSAuth():

    authorized = False

    def verify_code(self, code):
        print(f'Verifying code {code}')
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    # read more about this argument passing
    def __init__(self, security_code, authorizer: SMSAuth):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        # calling from SMSAuth class
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")

        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


# don't need SMS code verification
class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):

    # read more about this argument passing
    def __init__(self, email_address, authorizer: SMSAuth):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self, order):
        # calling from SMSAuth class
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())

authorizer = SMSAuth()
authorizer.verify_code(465839)

processor = DebitPaymentProcessor("2349875", authorizer)
processor.pay(order)