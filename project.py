class Store:
    def __init__(self):
        self.inventory = {}

    def add_product(self, name, quantity, cost, price):
        if name not in self.inventory:
            self.inventory[name] = {'quantity': quantity, 'cost': cost, 'price': price, 'sold': 0}
            return f"{quantity} units of {name} added to inventory."
        else:
            return "Product already exists in inventory. Use update_product to modify."

    def update_product(self, name, quantity=None, cost=None, price=None):
        if name in self.inventory:
            if quantity is not None:
                self.inventory[name]['quantity'] += quantity
            if cost is not None:
                self.inventory[name]['cost'] = cost
            if price is not None:
                self.inventory[name]['price'] = price
            return f"{name} updated in inventory."
        else:
            return "Product not found in inventory. Use add_product to add a new product."

    def record_sale(self, name, quantity):
        if name in self.inventory and self.inventory[name]['quantity'] >= quantity:
            self.inventory[name]['quantity'] -= quantity
            self.inventory[name]['sold'] += quantity
            return f"{quantity} units of {name} sold."
        else:
            return f"Not enough stock for {name}."

    def check_stock(self, name):
        if name in self.inventory:
            return f"Stock left for {name}: {self.inventory[name]['quantity']}"
        else:
            return f"{name} not found in inventory."

    def display_inventory(self):
        inventory_str = "\n=== Current Inventory ===\n"
        for product, details in self.inventory.items():
            inventory_str += f"{product}: Quantity - {details['quantity']}, Cost - {details['cost']}, Price - {details['price']}\n"
        return inventory_str

    def calculate_profit_loss(self, name):
        if name in self.inventory:
            total_cost = self.inventory[name]['cost'] * self.inventory[name]['sold']
            total_revenue = self.inventory[name]['price'] * self.inventory[name]['sold']
            profit_loss = total_revenue - total_cost
            return f"Profit/Loss for {name}: {profit_loss}"
        else:
            return f"{name} not found in inventory."


def display_menu():
    print("\n=== Store Management System ===")
    print("1. Add New Product")
    print("2. Update Existing Product")
    print("3. Record Sale")
    print("4. Check Stock")
    print("5. Display Inventory")
    print("6. Calculate Profit/Loss")
    print("7. Exit")


def perform_operation(store, choice):
    if choice == '1':
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity in stock: "))
        cost = float(input("Enter cost per unit: "))
        price = float(input("Enter selling price per unit: "))
        result = store.add_product(name, quantity, cost, price)
        print(result)

    elif choice == '2':
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity to add: "))
        cost = float(input("Enter new cost per unit: "))
        price = float(input("Enter new selling price per unit: "))
        result = store.update_product(name, quantity, cost, price)
        print(result)

    elif choice == '3':
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity sold: "))
        result = store.record_sale(name, quantity)
        print(result)

    elif choice == '4':
        name = input("Enter product name: ")
        result = store.check_stock(name)
        print(result)

    elif choice == '5':
        result = store.display_inventory()
        print(result)

    elif choice == '6':
        name = input("Enter product name: ")
        result = store.calculate_profit_loss(name)
        print(result)

    elif choice == '7':
        print("Exiting program. Thank you!")
        exit()

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    store = Store()

    while True:
        display_menu()
        user_choice = input("Enter your choice (1-7): ")
        perform_operation(store, user_choice)

