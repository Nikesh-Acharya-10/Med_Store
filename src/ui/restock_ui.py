"""
Restock transaction UI module.
"""

from src.core.inventory import display_inventory, save_inventory
from src.core.invoices import generate_restock_invoice


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            print("  [!] Please enter a valid positive whole number.")
        except ValueError:
            print("  [!] Invalid input. Please enter a whole number.")


def get_unit_type():
    while True:
        unit = input("  Restock by (T)ablet or (S)trip? ").strip().upper()
        if unit in ("T", "S"):
            return "tablet" if unit == "T" else "strip"
        print("  [!] Enter 'T' for tablet or 'S' for strip.")


def process_restock(medicines):
    print("\n" + "=" * 150)
    print("           RESTOCK TRANSACTION")
    print("=" * 150)

    supplier_name = input("  Supplier / Vendor name: ").strip()
    if not supplier_name:
        supplier_name = "Unknown Supplier"

    order = []
    total_cost = 0.0

    while True:
        print("\n  --- Add item to restock ---")
        display_inventory(medicines)

        while True:
            choice = input("  Enter medicine number (or 0 to cancel): ").strip()
            if choice == "0":
                break
            if choice.isdigit() and 1 <= int(choice) <= len(medicines):
                medicine = medicines[int(choice) - 1]
                break
            print(f"  [!] Enter a number between 1 and {len(medicines)}.")

        if choice == "0":
            if not order:
                print("  No items added. Returning to main menu.")
                return
            break

        unit_type = get_unit_type()
        quantity = get_positive_int(f"  Quantity ({unit_type}s): ")

        while True:
            try:
                rate = float(input(f"  Rate per {unit_type} (Rs): ").strip())
                if rate > 0:
                    break
                print("  [!] Rate must be greater than 0.")
            except ValueError:
                print("  [!] Please enter a valid number.")

        if unit_type == "tablet":
            tablets_added = quantity
        else:
            tablets_added = quantity * medicine["tablets_per_strip"]

        item_total = round(quantity * rate, 2)
        total_cost = round(total_cost + item_total, 2)

        print(f"\n  Medicine  : {medicine['name']} ({medicine['brand']})")
        print(f"  Quantity  : {quantity} {unit_type}(s)  = {tablets_added} tablets")
        print(f"  Item Cost : Rs {item_total:.2f}")

        order.append({
            "name": medicine["name"],
            "brand": medicine["brand"],
            "unit_type": unit_type,
            "quantity": quantity,
            "rate": rate,
            "total": item_total,
            "_medicine": medicine,
            "_tablets_added": tablets_added,
        })

        more = input("\n  Add another medicine? (Y/N): ").strip().upper()
        if more != "Y":
            break

    if not order:
        print("  No items in order. Returning to main menu.")
        return

    print("\n" + "=" * 150)
    print(f"  RESTOCK SUMMARY  —  Supplier: {supplier_name}")
    print("=" * 150)
    for item in order:
        print(f"  {item['name']:<25} {item['quantity']} {item['unit_type']}(s)  Rs {item['total']:>8.2f}")
    print("-" * 150)
    print(f"  {'GRAND TOTAL':<25}  Rs {total_cost:>8.2f}")
    print("=" * 150)

    confirm = input("\n  Confirm restock? (Y/N): ").strip().upper()
    if confirm != "Y":
        print("  Restock cancelled. No changes made.")
        return

    for item in order:
        item["_medicine"]["stock"] += item["_tablets_added"]
    save_inventory(medicines)

    invoice_items = [
        {k: v for k, v in item.items() if not k.startswith("_")}
        for item in order
    ]
    filename = generate_restock_invoice(supplier_name, invoice_items, total_cost)
    print(f"\n  Restock complete! Note saved: {filename}")
