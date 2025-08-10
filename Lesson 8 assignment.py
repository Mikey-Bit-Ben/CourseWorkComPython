print("Welcome to the contact manager app")
print("___________________________________________")
def main():
    print("1 - Create a new contact CSV file")
    print("2 - Add a new contact to the CSV file")
    print("3 - View all contacts")
    print("4 - modify a contact")
    print("5 - Save and Exit the app")
    option = input("Please enter your choice (1-5): ")
    if option == '1':
        create_contact_file()
    elif option == '2':
        add_contact()
    elif option == '3':
        view_contacts()
    elif option == '4':
        modify_contact()
    elif option == '5':
        print("Exiting the app. Goodbye!")
        print("completed by, John Benites")
        exit()
    else:
        print("Invalid option. Please try again.")
        main()

def create_contact_file():
    #creates a new CSV file for contacts
    with open('contacts.csv', 'w') as file:
        file.write("Name,Phone,Email\n")
    print("Contact file created successfully.")
    main()
def add_contact():
    #adds a new contact to the CSV file by taking user input and appending it to the file
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    email = input("Enter contact email: ")
    with open('contacts.csv', 'a') as file:
        file.write(f"{name}\t\t{phone}\t{email}\n")
    print("Contact added successfully.")
    main()
def view_contacts():
#views all contacts in the CSV file, displaying them in a formatted way and handling the case where the file might not exist
    with open('contacts.csv', 'r') as file:
            contacts = file.readlines()
            if len(contacts) <= 1:
                print("No contacts found.")
                main()
            else:
                print("Contacts Information:")
                print("__________________________________________")
                print("Name\t\tPhone\t\tEmail")
                for contact in contacts[1:]:  # Skip header
                    print(contact.strip())
                main()
    if FileNotFoundError:
        print("Contact file not found. Please create a contact file first.")
        main()
def modify_contact():
#modifies an existing contact by searching for it in the CSV file and allowing the user to update its details
    with open('contacts.csv', 'r') as file:
        contacts = file.readlines()
        print("Current contacts:")
        print("name\t\tPhone\t\tEmail")
        for contact in contacts[1:]:
            print(contact.strip())
        contact_name = input("Enter the name of the contact to modify: ")
        for i, contact in enumerate(contacts[1:], start=1):
            if contact_name in contact:
                print("Current contact details:", contact.strip())
                new_phone = input("Enter new phone (leave blank to keep current): ")
                new_email = input("Enter new email (leave blank to keep current): ")
                # If the user leaves a field blank, keep the current value
                if not new_phone:
                    new_phone = contact.split('\t')[0].strip()
                if not new_email:
                    new_email = contact.split('\t')[1].strip()
                # Updates the contact in the list
                contacts[i] = f"{contact_name}\t\t{new_phone}\t{new_email}\n"
                with open('contacts.csv', 'w') as file:
                    file.writelines(contacts)
                print("Contact modified successfully.")
                main()
        else:
            print("Contact not found.")
            main()
if __name__ == '__main__':
    main()
