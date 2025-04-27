contacts = {}

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def search_contact(contacts):
    name = input("Enter contact name to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print(f"Contact '{name}' not found.")

def update_contact(contacts):
    name = input("Enter contact name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_contact(contacts)
    elif choice == '2':
        view_contacts(contacts)
    elif choice == '3':
        search_contact(contacts)
    elif choice == '4':
        update_contact(contacts)
    elif choice == '5':
        delete_contact(contacts)
    elif choice == '6':
        break
    else:
        print("Invalid choice! Please try again.")
