"""
this is the main python file for the MedStore Pvt. Ltd. wholesale medicine management system.
it serves as the entry point for the application, providing a user-friendly interface to manage inventory, process sales, and handle restocking of medicines. The system is designed to be simple and efficient, allowing users to easily navigate through the various functionalities of the application.
This file import all the necessary modules and functions from the inventory, sales, and restock modules to perform the required operations. It also includes functions to display the main menu and handle user input for different actions. The main function orchestrates the flow of the application, ensuring that users can view inventory, sell medicines, restock as needed, and exit the system gracefully.
The main features of this file include:
Displaying
sale and restock options to the user
Handling user input and validating choices
and the flow of the program based on the user interactions.
"""

from inventory import load_inventory, display_inventory
from sales import process_sale
from restock import process_restock

# Function to print the header of the application
def print_header():
    print("\n" + "=" * 100)
    print("         MEDSTORE PVT. LTD.")
    print("      Wholesale Medicine Management")
    print("=" * 100)

# Function to display the main menu options to the user
def print_menu():
    print("\n  MAIN MENU")
    print("  ---------")
    print("  1. View Inventory")
    print("  2. Sell Medicines")
    print("  3. Restock Medicines")
    print("  4. Exit")
    print()

# Main function to run the MedStore application
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


if __name__ == "__main__":
    main()
