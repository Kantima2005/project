class Store:
    def __init__(self):
        self.inventory = {}

    def add_product(self, name, quantity, cost, price):
        if name not in self.inventory:
            self.inventory[name] = {'quantity': quantity, 'cost': cost, 'price': price, 'sold': 0}
            print(f"{quantity} units of {name} added to inventory.")
        else:
            print("Product already exists in inventory. Use update_product to modify.")

    def record_sale(self, name, quantity):
        if name in self.inventory and self.inventory[name]['quantity'] >= quantity:
            self.inventory[name]['quantity'] -= quantity
            self.inventory[name]['sold'] += quantity
            print(f"{quantity} units of {name} sold.")
        else:
            print(f"Not enough stock for {name}.")

    def check_stock(self, name):
        if name in self.inventory:
            return self.inventory[name]['quantity']
        else:
            return 0

    def display_inventory(self):
        print("\n=== Current Inventory ===")
        for product, details in self.inventory.items():
            print(f"{product}: Quantity - {details['quantity']}, Cost - {details['cost']}, Price - {details['price']}")

    def calculate_profit_loss(self, name):
        if name in self.inventory:
            total_cost = self.inventory[name]['cost'] * self.inventory[name]['sold']
            total_revenue = self.inventory[name]['price'] * self.inventory[name]['sold']
            profit_loss = total_revenue - total_cost
            return profit_loss
        else:
            return 0

# Function to display menu
def display_menu():
    print("\n=== Store Management System ===")
    print("1. Add Product to Inventory")
    print("2. Record Sale")
    print("3. Check Stock")
    print("4. Display Inventory")
    print("5. Calculate Profit/Loss")
    print("6. Exit")

# Example usage:
store = Store()

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity in stock: "))
        cost = float(input("Enter cost per unit: "))
        price = float(input("Enter selling price per unit: "))
        store.add_product(name, quantity, cost, price)

    elif choice == '2':
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity sold: "))
        store.record_sale(name, quantity)

    elif choice == '3':
        name = input("Enter product name: ")
        stock = store.check_stock(name)
        print(f"Stock left for {name}: {stock}")

    elif choice == '4':
        store.display_inventory()

    elif choice == '5':
        name = input("Enter product name: ")
        profit_loss = store.calculate_profit_loss(name)
        print(f"Profit/Loss for {name}: {profit_loss}")

    elif choice == '6':
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")