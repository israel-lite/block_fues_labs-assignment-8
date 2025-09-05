class ShoppingCart:
    def __init__(self, price_list):
        self.price_list = price_list
        self.items = {}

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item] > quantity:
                self.items[item] -= quantity
            else:
                print(f"{quantity} is greater than the available quantity of {item}")
        else:
            print(f"{item}, not in cart!")


record = ShoppingCart({"Shirt": 5000, "Shoes": 12000})

# record.add_item("Shirt", 2) 

record.add_item("Shoes", 3)

record.remove_item("Shoes", 5)
print(record.items)
