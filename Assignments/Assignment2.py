# Real world application using control structures
# Assignment 2: E-Commerce Platform with Login System and Price Calculator

# ============================================================
#  USER DATABASE (username: [password, role])
# ============================================================
users = {
    "admin":    ["admin123",    "Admin"],
    "john":     ["john456",     "Customer"],
    "jane":     ["jane789",     "Customer"],
    "cashier1": ["cash111",     "Cashier"],
}

# ============================================================
#  VALID COUPON CODES (code: discount percentage)
# ============================================================
coupon_codes = {
    "SAVE10":  10,
    "SAVE20":  20,
    "HALFOFF": 50,
}

# ============================================================
#  TAX RATES BY LOCATION (location: tax percentage)
# ============================================================
tax_rates = {
    "Uganda":  18,   # VAT
    "Kenya":   16,
    "USA":     8,
    "UK":      20,
    "Other":   15,
}


# ============================================================
#  PART 1 — LOGIN SYSTEM
# ============================================================
def login():
    """Check user credentials and return their role."""
    print("=" * 40)
    print("   Welcome to ShopEasy E-Commerce")
    print("=" * 40)

    username = input("Enter username: ").strip().lower()
    password = input("Enter password: ").strip()

    # Check if username exists
    if username in users:
        stored_password = users[username][0]
        role            = users[username][1]

        # Check if password is correct
        if password == stored_password:
            print(f"\n✅ Login successful! Welcome, {username}.")
            print(f"   Your role: {role}")
            return username, role
        else:
            print("\n❌ Incorrect password. Access denied.")
            return None, None
    else:
        print("\n❌ Username not found. Access denied.")
        return None, None


# ============================================================
#  PART 2 — ACCESS LEVELS
# ============================================================
def show_access(role):
    """Show what the user is allowed to do based on their role."""
    print("\n--- Your Access Level ---")

    if role == "Admin":
        print("✔ View all products")
        print("✔ Add / remove products")
        print("✔ View all orders")
        print("✔ Manage users")
        print("✔ Process payments")

    elif role == "Customer":
        print("✔ Browse products")
        print("✔ Add items to cart")
        print("✔ Place orders")
        print("✘ Cannot manage users or products")

    elif role == "Cashier":
        print("✔ View products")
        print("✔ Process payments")
        print("✔ View orders")
        print("✘ Cannot manage users or add products")

    else:
        print("✘ Unknown role — no access granted.")


# ============================================================
#  PART 3 — PRICE CALCULATOR
# ============================================================
def calculate_price():
    """Calculate the final price using subtotal, discount, coupon, and tax."""
    print("\n" + "=" * 40)
    print("       Price Calculator")
    print("=" * 40)

    # --- Get subtotal ---
    subtotal = float(input("Enter the subtotal (product price): $"))

    # Validate subtotal
    if subtotal <= 0:
        print("❌ Subtotal must be greater than zero.")
        return

    # --- Automatic discount based on subtotal amount ---
    print("\n--- Subtotal Discount ---")
    if subtotal >= 500:
        auto_discount = 15
        print(f"🎉 Big spender! You get a 15% discount (order over $500).")
    elif subtotal >= 200:
        auto_discount = 10
        print(f"🎉 You get a 10% discount (order over $200).")
    elif subtotal >= 100:
        auto_discount = 5
        print(f"🎉 You get a 5% discount (order over $100).")
    else:
        auto_discount = 0
        print("No automatic discount (order under $100).")

    # --- Coupon code ---
    print("\n--- Coupon Code ---")
    coupon_input = input("Enter a coupon code (or press Enter to skip): ").strip().upper()

    if coupon_input == "":
        coupon_discount = 0
        print("No coupon applied.")
    elif coupon_input in coupon_codes:
        coupon_discount = coupon_codes[coupon_input]
        print(f"✅ Valid coupon! Extra {coupon_discount}% off.")
    else:
        coupon_discount = 0
        print("❌ Invalid coupon code. No extra discount applied.")

    # --- Total discount (we don't let it exceed 60%) ---
    total_discount_percent = auto_discount + coupon_discount
    if total_discount_percent > 60:
        total_discount_percent = 60
        print("ℹ️  Maximum discount capped at 60%.")

    discount_amount = subtotal * (total_discount_percent / 100)
    price_after_discount = subtotal - discount_amount

    # --- Tax based on location ---
    print("\n--- Tax ---")
    print("Available locations:", ", ".join(tax_rates.keys()))
    location = input("Enter your location: ").strip().title()

    if location in tax_rates:
        tax_rate = tax_rates[location]
    else:
        tax_rate = tax_rates["Other"]
        print(f"Location not listed. Using default tax rate of {tax_rate}%.")

    tax_amount = price_after_discount * (tax_rate / 100)
    final_price = price_after_discount + tax_amount

    # --- Receipt ---
    print("\n" + "=" * 40)
    print("           RECEIPT")
    print("=" * 40)
    print(f"  Subtotal:              ${subtotal:.2f}")
    print(f"  Auto discount ({auto_discount}%):   -${subtotal * auto_discount / 100:.2f}")
    print(f"  Coupon discount ({coupon_discount}%): -${subtotal * coupon_discount / 100:.2f}")
    print(f"  Price after discount:  ${price_after_discount:.2f}")
    print(f"  Tax ({tax_rate}% - {location}):     +${tax_amount:.2f}")
    print("-" * 40)
    print(f"  FINAL PRICE:           ${final_price:.2f}")
    print("=" * 40)


# ============================================================
#  MAIN PROGRAM — puts it all together
# ============================================================
def main():
    # Step 1: Login
    username, role = login()

    # If login failed, stop the program
    if role is None:
        return

    # Step 2: Show what the user can access
    show_access(role)

    # Step 3: Only Admin and Cashier can use the price calculator
    print("\n--- Price Calculator Access ---")
    if role == "Admin" or role == "Cashier":
        use_calc = input("Would you like to use the price calculator? (yes/no): ").strip().lower()
        if use_calc == "yes":
            calculate_price()
        else:
            print("Okay! Exiting the calculator.")
    elif role == "Customer":
        print("As a Customer, you can browse and order — the price calculator is for staff.")
    
    print("\nThank you for using ShopEasy. Goodbye! 👋")


# Run the program
main()
