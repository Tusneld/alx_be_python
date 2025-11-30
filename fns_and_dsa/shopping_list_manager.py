"""
1. Shopping List Manager
Objective: Utilize Python lists to create a simple shopping list manager that allows 
           users to add items, view the current list, and remove items.
"""

def display_menu():
    """Prints the menu options for the shopping list manager."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # Initialize the core data structure: an empty list
    shopping_list = []
    
    # Use an infinite loop to keep the program running until the user chooses to exit
    while True:
        # Display a newline before the menu for better readability in the terminal
        print()       
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # --- Add Item Functionality ---
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")
            
        elif choice == '2':
            # --- Remove Item Functionality ---
            item_to_remove = input("Enter the item to remove: ").strip()
            
            # Use a try-except block to handle cases where the item is not found
            try:
                # Remove the item from the list       
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list.")
            except ValueError:
                # This exception is raised if item_to_remove is not in the list
                print(f"Error: '{item_to_remove}' not found in the list.")
                
        elif choice == '3':
            # --- View List Functionality ---
            if shopping_list:
                print("\n--- Current Shopping List ---")
                # Iterate through the list and print each item with a number
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
                print("---------------------------")
            else:
                print("The shopping list is empty.")
            
        elif choice == '4':
            # --- Exit Functionality ---
            print("Goodbye!")
            break
            
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":

    main()
