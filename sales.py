
from inventory import display_inventory, save_inventory
from calculator import calculate_tablet_sale, calculate_strip_sale
from invoice import generate_sale_invoice

#function for the user input for the quantatiy from the user
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            print("Please enter a valid positive whole number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

#takes the imput from the user as a form of tablet or string
def get_unit_type():
    while True:
        unit = input("  Sell by (T)ablet or (S)trip? ").strip().upper()
        if unit in ("T", "S"):
            return "tablet" if unit == "T" else "strip"
        print("   Enter 'T' for tablet or 'S' for strip.")


def pick_medicine(medicines):
   
    display_inventory(medicines)
    while True:
        choice = input("  Enter medicine number (or 0 to cancel): ").strip()
        if choice == "0":
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(medicines):
            return medicines[int(choice) - 1]
        print(f"  Enter a number between 1 and {len(medicines)}.")


def process_sale(medicines):
  
    print("\n" + "=" * 150)
    print("           SALE TRANSACTION")
    print("=" * 150)

    customer_name = input("  Customer name: ").strip()
    if not customer_name:
        customer_name = "Walk-in Customer"

    cart = []          
    total_bill = 0.0

    while True:
        print("\n   Add item to cart ")
        medicine = pick_medicine(medicines)
        if medicine is None:
            if not cart:
                print("  No items added. Returning to main menu.")
                return
            break  

        unit_type = get_unit_type()
        quantity = get_positive_int(f"  Quantity ({unit_type}s): ")

        #  Check stock for the requested quantity by a user and calculate how many tablets are needed for the sale based on unit type
        if unit_type == "tablet":
            tablets_needed = quantity
        else:
            tablets_needed = quantity * medicine["tablets_per_strip"]

        if tablets_needed > medicine["stock"]:
            available_strips = medicine["stock"] // medicine["tablets_per_strip"]
            print(f"  Not enough stock!")
            print(f"      Available: {medicine['stock']} tablets "
                  f"({available_strips} full strips)")
            continue

        #  Calculate price  for this item based on unit type and quantity
        if unit_type == "tablet":
            result = calculate_tablet_sale(
                quantity,
                medicine["rate_per_tablet"],
                medicine["rate_per_strip"],
                medicine["tablets_per_strip"],
            )
        else:
            result = calculate_strip_sale(
                quantity,
                medicine["rate_per_strip"],
                medicine["tablets_per_strip"],
            )

        #  Show item summary that will be added to cart
        print(f"\n  Medicine    : {medicine['name']} ({medicine['brand']})")
        if unit_type == "tablet" and result["strips"] >= 1:
            print(f"  Breakdown   : {result['strips']} strip(s) + "
                  f"{result['remaining_tablets']} tablet(s)")
        print(f"  Subtotal    : Rs {result['subtotal']:.2f}")
        if result["discount_applied"]:
            print(f"  Discount(5%): Rs {result['discount_amount']:.2f}")
        print(f"  Item Total  : Rs {result['total']:.2f}")

        cart_item = {
            "name":              medicine["name"],
            "brand":             medicine["brand"],
            "unit_type":         unit_type,
            "quantity":          quantity,
            "strips":            result.get("strips", 0),
            "remaining_tablets": result.get("remaining_tablets", quantity),
            "subtotal":          result["subtotal"],
            "discount_applied":  result["discount_applied"],
            "discount_amount":   result["discount_amount"],
            "total":             result["total"],
            "_medicine":         medicine,
            "_tablets_needed":   tablets_needed,
        }
        cart.append(cart_item)
        total_bill = round(total_bill + result["total"], 2)
        print(f"\n  Running total: Rs {total_bill:.2f}")

        more = input("\n  Add another medicine? (Y/N): ").strip().upper()
        if more != "Y":
            break

    if not cart:
        print("  No items in cart. Returning to main menu.")
        return
# Generate and save invoice
    print("\n" + "=" * 150)
    print(f"  BILL SUMMARY  —  Customer: {customer_name}")
    print("=" * 150)
    for item in cart:
        print(f"  {item['name']:<25}  Rs {item['total']:>8.2f}")
    print("-" * 150)
    print(f"  {'GRAND TOTAL':<25}  Rs {total_bill:>8.2f}")
    print("=" * 150)

    confirm = input("\n  Confirm sale? (Y/N): ").strip().upper()
    if confirm != "Y":
        print("  Sale cancelled. No changes made.")
        return

    for item in cart:
        item["_medicine"]["stock"] -= item["_tablets_needed"]
    save_inventory(medicines)
# Generate invoice for the sale
    invoice_items = [
        {k: v for k, v in item.items() if not k.startswith("_")}
        for item in cart
    ]
    filename = generate_sale_invoice(customer_name, invoice_items, total_bill)

    print(f"\n  Sale complete! Invoice saved: {filename}")
