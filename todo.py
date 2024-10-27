# file path
file_path = 'tasks.json'

# main menu function
def main_menu():
    print("\nMain Menu")
    print("1. Your To Do List")
    print("2. Add a Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")
    return choice


def run_application():
    
    while True:
        
        choice = main_menu()

        if choice == "1":
            print("you are in choice One")
        elif choice == "2":
            print("you are in choice Two")
        elif choice == "3":
            print("you are in choice Three")
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice")

run_application()