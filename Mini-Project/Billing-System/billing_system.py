# SkillNexis Python Programming
# Week 3 - Mini Project
# Billing System (OOP-based)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self, tax_rate=5):
        self.products = []
        self.tax_rate = tax_rate

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        return sum(product.get_total() for product in self.products)

    def calculate_tax(self):
        return self.calculate_subtotal() * self.tax_rate / 100

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self):
        print("\n" + "=" * 60)
        print("                    FINAL BILL")
        print("=" * 60)

        print(f"{'Product':<20}{'Price':>10}{'Qty':>10}{'Total':>15}")
        print("-" * 60)

        for product in self.products:
            print(
                f"{product.name:<20}"
                f"₹{product.price:>9.2f}"
                f"{product.quantity:>10}"
                f"₹{product.get_total():>14.2f}"
            )

        print("-" * 60)

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()

        print(f"{'Subtotal':<45}₹{subtotal:>14.2f}")
        print(f"{'Tax (5%)':<45}₹{tax:>14.2f}")
        print(f"{'Grand Total':<45}₹{total:>14.2f}")
        print("=" * 60)


print("========================================")
print("          BILLING SYSTEM")
print("========================================")

bill = Bill()

while True:
    print("\n1. Add Product")
    print("2. Generate Bill")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter product name: ")

        try:
            price = float(input("Enter product price: ₹"))
            quantity = int(input("Enter quantity: "))

            if price <= 0 or quantity <= 0:
                print("Price and quantity must be greater than zero.")
            else:
                product = Product(name, price, quantity)
                bill.add_product(product)
                print("Product added successfully!")

        except ValueError:
            print("Please enter valid numbers.")

    elif choice == "2":
        if not bill.products:
            print("No products added.")
        else:
            bill.display_bill()

    elif choice == "3":
        print("Thank you for using the Billing System!")
        break

    else:
        print("Invalid choice. Please try again.")