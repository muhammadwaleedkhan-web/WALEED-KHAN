# Inventory Management System


class Product:
    def __init__(self, name, price, quantity):
#These are the objects in which data will be stored
        self.name = name
        self.price = price
        self.quantity = quantity

#function to display the information of the product
    def display_info(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("this is the information about the product")



inventory = {}          # for creating key and putting its values in the inventory to save
categories = set()      # for tracking the product category
actions = []             # making a tuple for show last three actions


def record_action(action):
    global actions
    actions.insert(0, action)  #for adding a new action at the start
if len(actions) > 3:  # for showing the last three actions from tuple
    actions = actions[0:3]
3
#required functions to add remove update product
#adding a new product to inventory
def add_product(inventory, name, price, quantity, category):
    if name in inventory:
        print(f"{name} already exists!")
        return
#making variable to store objects data
    product = Product(name, price, quantity)
    inventory[name] = product
    categories.add(category)

    record_action(f"Added {name}")
    print(f"{name} added successfully!\n")
#function for updating the product in inventory dictionary
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

    record_action(f"Updated quantity of {name}")
    print(f"Quantity updated! New quantity: {inventory[name].quantity}\n")
#making a function for removing a product from the inventory dictionary
def remove_product(inventory, name):
    if name in inventory:
        del inventory[name]
        record_action(f"Removed {name}")
        print(f"{name} removed successfully!")
    else:
        print(f"{name} not found!")
        return
#making a function to search the product

def search_product(inventory, name):
    if name in inventory:
        print("Product Found:")
        inventory[name].display_info()
    else:
        print(f"{name} not found!")
        return
#making a function to display information
def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty!")
        return

    print("---- Inventory ----")
    for product in inventory.values():
        product.display_info()

    print("Categories:", categories)
    print("Last 3 Actions:", actions)
    print()

#Making a user menu by using loops and contionals
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
    choice = input("Enter your choice (1–6): ")

    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter quantity: "))
        category = input("Enter category: ")

        add_product(inventory, name, price, quantity, category)

    elif  choice == "2":
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
        print("Thanks for using our inventory managment system ")
        break

    else:
        print("You have chosen Invalid choice! Please enter a number from 1 to 6.")


