import json

# file path
file_path = 'tasks.json'

# main menu function
def main_menu():

    print("\nMain Menu:")
    print("1. Your To Do List") #
    print("2. Add a Task") 
    print("3. Edit a Task")
    print("4. Remove a Task")
    print("5. Exit") 
   

    choice = input("Enter your choice: ")
    return choice

def display_list():
    try:
        with open(file_path, "r") as f:
            


            file_data = json.load(f)

            index = 1

            if(len(file_data) == 0):
                print("\nYou dont have anything in your List.")
                choice = input("\nWould you like to add a New Task?\n (Y/N)")

                if(choice == "y" or choice == "Y"):
                    print("Yes")
                else:
                    print("no")
            
            else:
                print("\nYour To Do List:")
                for task in file_data:
                    print(f"{index}.", task["description"])
                    index += 1

        
    except:
        print("Error to read the file")
    


def run_application():
    
    while True:
        
        choice = main_menu()

        if choice == "1":
            display_list()
        elif choice == "2":
            print("you are in choice Two")
        elif choice == "3":
            print("you are in choice Three")
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    run_application()