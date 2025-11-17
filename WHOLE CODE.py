# Inventory Management System

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("This is the information about the product")


inventory = {}
categories = set()
actions = []


def record_action(action):
    global actions
    actions.insert(0, action)
    if len(actions) > 3:
        actions = actions[0:3]


def add_product(inventory, name, price, quantity, category):
    if name in inventory:
        print(f"{name} already exists!")
        return

    product = Product(name, price, quantity)
    inventory[name] = product
    categories.add(category)

    record_action(f"Added {name}")
    print(f"{name} added successfully!\n")


def update_quantity(inventory, name, change):
    if name not in inventory:
        print(f"{name} not found!")
        return

    product = inventory[name]
    product.quantity += change

    if product.quantity < 0:
        product.quantity = 0

    record_action(f"Updated quantity of {name} to {product.quantity}")
    print(f"Quantity updated! New quantity: {product.quantity}\n")


def remove_product(inventory, name):
    if name in inventory:
        del inventory[name]
        record_action(f"Removed {name}")
        print(f"{name} removed successfully!\n")
    else:
        print(f"{name} not found!")


def search_product(inventory, name):
    if name in inventory:
        print("Product Found:")
        inventory[name].display_info()
    else:
        print(f"{name} not found!")


def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty!")
        return

    print("\n----- Inventory -----")
    for product in inventory.values():
        product.display_info()

    print("Categories:", categories)
    print("Last 3 Actions:", actions)
    print()


while True:
    print("""
    Inventory Management Menu:
    1. Add Product
    2. Update Quantity
    3. Remove Product
    4. Display Inventory
    5. Search Product
    6. Exit
    """)
    choice = input("Enter your choice (1 to 6): ")

    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter quantity: "))
        category = input("Enter category: ")
        add_product(inventory, name, price, quantity, category)

    elif choice == "2":
        name = input("Enter product name: ")
        change = int(input("Enter quantity change (+/-): "))
        update_quantity(inventory, name, change)

    elif choice == "3":
        name = input("Enter product name: ")
        remove_product(inventory, name)

    elif choice == "4":
        display_inventory(inventory)

    elif choice == "5":
        name = input("Enter product name: ")
        search_product(inventory, name)

    elif choice == "6":
        print("Exiting program...")
        print("Thanks for using our inventory management system!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 6.")
