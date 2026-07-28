"""
Main application UI and menu system.
"""

from src.core.inventory import load_inventory, display_inventory
from src.ui.sales_ui import process_sale
from src.ui.restock_ui import process_restock


def print_header():
    print("\n" + "=" * 100)
    print("         MEDSTORE PVT. LTD.")
    print("      Wholesale Medicine Management")
    print("=" * 100)


def print_menu():
    print("\n  MAIN MENU")
    print("  ---------")
    print("  1. View Inventory")
    print("  2. Sell Medicines")
    print("  3. Restock Medicines")
    print("  4. Exit")
    print()


def main():
    print_header()
    medicines = load_inventory()

    while True:
        print_menu()
        choice = input("  Enter your choice (1-4): ").strip()

        if choice == "1":
            display_inventory(medicines)

        elif choice == "2":
            if not medicines:
                print("\n  ! No medicines in inventory. Please restock first.")
            else:
                process_sale(medicines)

        elif choice == "3":
            process_restock(medicines)

        elif choice == "4":
            print("\n  Goodbye, Closing MedStore System.\n")
            break

        else:
            print("   Invalid choice. Please enter a number between 1 and 4.")
