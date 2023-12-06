#!/usr/bin/env python3

# cash_register.py

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # Format the total without cents
            formatted_total = f"{self.total:.0f}"
            print(f"After the discount, the total comes to ${formatted_total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.total - sum([price for _, price, _ in self.items[:-1]])
            self.total = last_item_price
            print(f"Voided the last transaction. Updated total is ${self.total:.2f}.")
        else:
            print("No transactions to void.")

# Additional helper class to store items with prices for each transaction
class TransactionItem:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

if __name__ == "__main__":
    # You can add additional testing here or in a separate test file
    pass
