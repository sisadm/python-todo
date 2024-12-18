import json

import os

# file path
file_path = 'tasks.json'


# file reading function 
def read_file():
    with open(file_path, "r") as f:
        return json.load(f)

# write into file function
def write_file(new_data):
        # opening to write
    with open(file_path, 'w') as file_write:
        
        # dump back the data with the new dictionary
        json.dump(new_data, file_write, indent=4)

# display the list
def display_again():
    print("\nHere is the new To Do List:\n")
    display_list()
    


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

    # checking the file contains anything
    is_empty = os.stat(file_path).st_size

    if(is_empty == 0):
        
        print("\nYou dont have anything in your List.")
        choice = input("\nWould you like to add a New Task?\n (Y/N)")

        if(choice == "y" or choice == "Y"):
            add_task()
        else:
            return 

    # if it has loop through each element and display it
    else:
        # opening the json file
        try:
                # calling read_file function
                file_data = read_file()

                index = 1

                print("\nYour To Do List:")

                for task in file_data:
                    print(f"{index}.", task["description"], " status:", task["status"])
                    index += 1

            
        except:
            print("Error to read the file")
        

def add_task():
    # input from user
    description = input("\nYour task: ")
    status = input("\nStatus: ")

    # save as a dictionary
    new_data = {
            "description": description,
            "status" : status
    }

    # opening the file for read
    try:
        data = read_file()

    except (json.JSONDecodeError, FileNotFoundError):
        # if something went wrong creating an empty array
        data = []        

    # adding the new data into the loaded json data
    data.append(new_data)

    # write it into the jsone file
    write_file(data)

    display_again()



def edit_remove_task(command):

    # display the list existing list
    display_list()

    # get an input
    print("\nWhich task would you like to change?")
    number = input("Please write the number: ")
    


    try:

        # calling read_file function
        file_data = read_file()

        # edit task
        if(command == "edit"):
            which_part = input("\nWhat would you want to change?(description/status) ")
            

            if(which_part.lower() == "description"):
                new_description = input("Enter the new description: ")
                file_data[(int(number) - 1)]["description"] = new_description
                write_file(file_data)
            
            elif(which_part.lower() == "status"):
                new_status = input("Enter the new description: ")
                file_data[(int(number) - 1)]["status"] = new_status
                write_file(file_data)
            else:
                print("\nPlease type description or status into the field.")
        
        # remove task
        else:
            # pop the targeted number directory 
            file_data.pop(number)
            write_file(file_data)

    except:
        print("Error to read the file")
        
    display_again()
    
    

def run_application():
    
    while True:
        
        choice = main_menu()

        if choice == "1":
            display_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            edit_remove_task("edit")
        elif choice == "4":
            edit_remove_task("remove")
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    run_application()