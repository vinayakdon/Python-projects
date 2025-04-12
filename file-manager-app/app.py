import os

# Helps to create a file
def create_file(filename):
    try:
        with open(filename, 'x') as file:
            print(f"{filename} file is created succesfully..")
    except FileNotFoundError:
        print(f"file {filename} is alread exist!")
    
    except Exception as E:
        print("An error occured.")

# Helps to see all the files in the directory
def view_all_files():
    files = os.listdir()
    if not files:
        print("No file Exist.")
    else:
        print("list of files: ")
        for file in files:
            print(file)

# Helps to Delete Particular file
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"file {filename} deleted successfully")
    except FileNotFoundError:
        print(f"file {filename} is not exist!")

    except Exception as E:
        print("An error occured.")

# Help to Read a content of the file
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"{filename} content show below: ")
            print(content)

    except FileNotFoundError:
        print(f"file {filename} is not exist!")

    except Exception as E:
        print("An error occured.")

# Help to write or add new content into the file
def edit_file(filename):
    try:
        with open(filename, 'a') as file:
            content = input("enter the data to add: ")
            file.write(content + "\n")
            print(f"content added to file {filename}.")

    except FileNotFoundError:
        print(f"file {filename} is not exist!")

    except Exception as E:
        print("An error occured.")

# Main function to display
def main():
    print("\n")
    while True:
        print("-----------------")
        print("File Manager App")
        print("-----------------")

        print('1. Create a File')
        print('2. View all Files')
        print('3. Delete a File')
        print('4. Read a File')
        print('5. edit a File')
        print('6. Exit')

        userChoice = input("Enter your choice from (1-6): ")

        if userChoice == "1":
            filename = input("Enter the filename to create: ")
            create_file(filename)

        elif userChoice == "2":
            view_all_files()

        elif userChoice == "3":
            filename = input("Enter the filename to delete: ")
            delete_file(filename)

        elif userChoice == "4":
            filename = input("Enter the filename to read: ")
            read_file(filename)

        elif userChoice == "5":
            filename = input("Enter the filename to edit: ")
            edit_file(filename)

        elif userChoice == "6":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice..")

if __name__ == "__main__":
    main()
