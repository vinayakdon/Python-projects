import json

def Create_contact():
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    mobileNo = input("Enter mobile number: ")
    return age , email, mobileNo


def View_contact():
    print("1. view all contacts")
    print("2. view perticular contact")
    user = input("Enter your choice: ")
    return user


def Update_contact():
    contactName = input("Enter the Contact name you wanted to update: ")
    return contactName


def Delete_contact():
    contact_name_to_delete = input("Enter the contact name to delete: ")
    return contact_name_to_delete

def Search_contact():
    contact_name_to_search = input("Enter contact you want to search")
    return contact_name_to_search

def main():
    contacts = {}
    while True:
        print("Contact Book App")
        print("1. Create contact")
        print("2. View contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Search contact")
        print("6. Count Contact")
        print("7. Exit")


        userChoice = input("Enter your choice: ")

        if userChoice == "1":
            name = input("Enter your name: ")
            if name in contacts:
                print(f"Contact name {name} already exist")
            else:
                [age, email, mobileNo] = Create_contact()
                contacts[name] = {'age': int(age), 'email': email, 'number': mobileNo}
                print("Contact created successfully")

        elif userChoice == "2":
            users = View_contact()
            if users == "1":
                if not contacts:
                    print("No contacts yet")
                else:
                    print(json.dumps(contacts, indent=4))
            else:
                viewreqcontact = input("Enter the contact name: ")
                if viewreqcontact in contacts:
                    print(json.dumps(contacts[viewreqcontact], indent=4))
                else:
                    print("requested name is not in the contact list")

        elif userChoice == "3":
            contact_name_to_update = Update_contact()
            if contact_name_to_update in contacts:
                print("Please specific what you want to update\n1.Age\n2.Email\n3.number")
                changeReq = input("Enter the choice: ")
                if changeReq == "1":
                    ageUpdate = int(input("Update age: "))
                    contacts[contact_name_to_update]["age"] = ageUpdate
                    print(f"{contact_name_to_update} Age Updated successfully")
                elif changeReq == "2":
                    emailUpdate = input("Update email: ")
                    contacts[contact_name_to_update]["email"] = emailUpdate
                    print(f"{contact_name_to_update} email Updated successfully")
                elif changeReq == "3":
                    numberUpdate = int(input("Update number: "))
                    contacts[contact_name_to_update]["number"] = numberUpdate
                    print(f"{contact_name_to_update} number Updated successfully")
                else:
                    print("Invalid choice")
            else:
                print(f"{contact_name_to_update} user not exist")

        elif userChoice == "4":
            contact_name_to_Delete = Delete_contact()
            if contact_name_to_Delete in contacts:
                del contacts[contact_name_to_Delete]
            else:
                print(f"{contact_name_to_Delete} user not exist") 
        
        elif userChoice == "5":
            contact_to_search = Search_contact()
            if contact_name_to_search in contacts:
                print(json.dumps(contacts[contact_name_to_search], indent=4))
            else:
                print("requested contact is not in the contact list")

        elif userChoice == "6":
            total_contacts = len(contacts)
            print(f"Total number of contacts in contact app: {total_contacts}")

        elif userChoice == "7":
            print("Exit from app")
            break
 
if __name__ == "__main__":
    main()