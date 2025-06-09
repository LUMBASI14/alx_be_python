 shopping_list = []
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item():
  item = input("Enter your item to the list: ")
  shopping_list.append(item)

def remove_item():
  item = input("Enter item to remove: ")
  shopping_list.remove(item)

def view_list():
  for item in shopping_list:
    print(item)


def main():
   
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item()
            pass
        elif choice == '2':
            remove_item()
            pass
        elif choice == '3':
            view_list()
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
  
