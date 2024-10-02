
name = ""

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            name = input("Enter the item to add: ")
            shopping_list.append(name)
            pass
        elif choice == '2':
            name = input("Enter the item to remove:")
            if name in shopping_list:
                shopping_list.remove(name)
            else:
                print("You entered an invalid item name")
            pass
        elif choice == '3':
            # Display the shopping list
            for item in shopping_list:
                print(item)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()