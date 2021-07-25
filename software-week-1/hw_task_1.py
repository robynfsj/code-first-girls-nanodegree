"""CFG Nanodegree Software Specialisation Homework 1 Task 1 – Cash Register"""

# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Write a class to represent a cash register.
# Your class should keep the state of price total and purchased items.
#
# Below is a starter code:
# ------------------------
# 1. You can add new variables and functions if you want to.
# 2. You will NEED to add accepted method parameters where required.
#    For example, method add_item probably accepts some kind of an item.
# 3. You will need to write some examples of how your code works.
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––


class CashRegister:

    def __init__(self):
        self.total_items = {}  # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    # This is instead of the reset_register method. I did it this way so that
    # this is always run at the start of a new transaction to be sure
    # everything is reset and that it prints the business name at the top of
    # the print out like you would have on a receipt.
    def new_transaction(self):
        self.total_items.clear()
        self.total_price = 0
        self.discount = 0
        welcome = "ROBYN'S CORNER SHOP"
        print(f"\n"
              f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              f"{welcome:^40}\n"
              f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def add_item(self, item, price):
        self.total_items[item.capitalize()] = price
        self.total_price += price
        print(f"{item.capitalize():>30s}{price:>10.2f}")

    def remove_item(self, item):
        try:
            removed = self.total_items.pop(item.capitalize())
        except KeyError:
            print("Item not found.")
        else:
            self.total_price -= removed
            item_str = f"*CANCELLED* {item.capitalize()}"  # Assign output messages to variables
            price_str = f"–{removed:.2f}"                  # so I can align within print function.
            print(f"{item_str:>30s}{price_str:>10}")

    def apply_discount(self, percentage_discount):
        self.discount = (percentage_discount/100) * self.total_price
        self.total_price = self.total_price - self.discount

    def get_total(self):
        print(f"————————————————————————————————————————")
        # Add discount details if discount was applied
        if self.discount:
            discount_str = "DISCOUNT APPLIED"
            discount_amount_str = f"-£{self.discount:.2f}"
            print(f"{discount_str:>30s}{discount_amount_str:>10}")
        total_str = "TOTAL"
        total_price_str = f"£{self.total_price:.2f}"
        print(f"{total_str:>30s}{total_price_str:>10}\n"
              f"————————————————————————————————————————")

    # This isn't really needed as I wanted the items to print out as they are
    # entered into the till because this is what would happen with a real till.
    # But have included it just in case it is required as it was part of the
    # starter code.
    def show_items(self):
        if not self.total_items:
            output = "No items added yet"
            print(f"{output:^40}")
        else:
            for item in self.total_items:
                price = f"£{self.total_items.get(item):.2f}"
                print(f"{item:>30s}{price:>10}")


# —————————————————————————————————————————————————————————————————————————————
# EXAMPLES OF CODE IN ACTION
# —————————————————————————————————————————————————————————————————————————————

# Create object of the CashRegister class.
till = CashRegister()

# Example customer with discount and changed mind about an item.
till.new_transaction()
till.add_item('bread', 1.10)
till.add_item('milk', 0.80)
till.add_item('picnic blanket', 12.50)
till.add_item('cornflakes', 2.80)
till.add_item('apples', 2.45)
till.add_item('wine', 11.00)
till.add_item('birthday cake', 7.50)
till.remove_item('picnic blanket')
till.apply_discount(15)
till.get_total()

# Example customer without discount
# Same till object used to demonstrate that new_transaction (i.e. register_rest) works.
till.new_transaction()
till.add_item('shampoo', 3.50)
till.add_item('pens', 2.40)
till.add_item('pencil case', 4.60)
till.add_item('chocolate bar', 0.75)
till.get_total()

# Example to prove that show_items works and that items are stored in
# total_items dict. (Although as I said early, not really needed as this code
# prints items as it goes like a normal till would.)
print("\n>>> till.show_items()")
till.show_items()
