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



        elif choice == "4":
            print("\n  Goodbye, Closing MedStore System.\n")
            break

        else:
            print("   Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
