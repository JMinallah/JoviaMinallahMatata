# Your Tasks
# Your job is to extend the functionality of the ContactManager class by 
# implementing the following requirements. Ensure you do not break the existing features.

# Task 1: Data Validation (20 Points)
# Currently, a user can enter any text for a phone number or email. 
# Modify the code to add basic validation:

# Phone Validation: In add_contact and update_contact, 
# ensure the phone number contains only digits and hyphens (e.g., "+256-701"). 
# If it contains illegal characters, print an error message and cancel the operation.

# Email Validation: Ensure that if an email is provided, it contains an @ symbol and a . (period).


# Task 2: Advanced Search (25 Points)
# The current Contacts method only filters by name and phone number.

# Modify Contactss so that it can also search by email.

# Write a helper method or modify the search printout so it displays the search results in a clean, 
# user-friendly format rather than just returning a raw Python list of tuples.


# Task 3: Interactive CLI Menu (35 Points)
# Create an interactive Command Line Interface (CLI) loop inside a function called main(). 
# When run, the program should present the user with a recurring menu until they choose to exit.

# The menu should look similar to this:

# === Contact Manager Menu ===CRUD
# 1. Add Contact
# 2. View Contact
# 3. Update Contact
# 4. Delete Contact
# 5. Search Contacts
# 6. List All Contacts
# 7. Exit
# Choose an option (1-7):

# Implement proper input handling for each menu item, 
# prompting the user for necessary arguments (like name, phone, etc.) 
# and passing them to your class methods.

# Submission Guidelines:
# 1. Add a single python script to your github link, 
# 2. Submit a single Python file named name_contact_assignment.py.

import sqlite3
import re
class ContactManager:
    def __init__(self, db_name="contacts.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT
                )
            ''')

    def validate_phone(self, phone):
        if re.match(r'^[\d-]+$', phone):
            return True
        print("Error: Phone number can only contain digits and hyphens.")
        return False

    def validate_email(self, email):
        if email and (re.match(r'^[^@]+@[^@]+\.[^@]+$', email)):
            return True
        print("Error: Invalid email format. Email must contain '@' and '.'.")
        return False

    def add_contact(self, name, phone, email=None):
        if not self.validate_phone(phone) or (email and not self.validate_email(email)):
            return
        with self.conn:
            self.conn.execute('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)', (name, phone, email))
            print("Contact added successfully.")

    def view_contact(self, contact_id):
        cursor = self.conn.execute('SELECT * FROM contacts WHERE id = ?', (contact_id,))
        contact = cursor.fetchone()
        if contact:
            print(f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}")
        else:
            print("Contact not found.")

    def update_contact(self, contact_id, name=None, phone=None, email=None):
        if phone and not self.validate_phone(phone):
            return
        if email and not self.validate_email(email):
            return
        with self.conn:
            contact = self.conn.execute('SELECT * FROM contacts WHERE id = ?', (contact_id,)).fetchone()
            if not contact:
                print("Contact not found.")
                return
            new_name = name if name else contact[1]
            new_phone = phone if phone else contact[2]
            new_email = email if email else contact[3]
            self.conn.execute('UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ?', 
                              (new_name, new_phone, new_email, contact_id))
            print("Contact updated successfully.")

    def delete_contact(self, contact_id):
        with self.conn:
            self.conn.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
            print("Contact deleted successfully.")
            
    def search_contacts(self, query):
        cursor = self.conn.execute('SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ? OR email LIKE ?', 
                                   (f'%{query}%', f'%{query}%', f'%{query}%'))
        results = cursor.fetchall()
        if results:
            print("Search Results:")
            for contact in results:
                print(f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}")
        else:
            print("No contacts found matching the query.")
            
    def list_contacts(self):
        cursor = self.conn.execute('SELECT * FROM contacts')
        contacts = cursor.fetchall()
        if contacts:
            print("All Contacts:")
            for contact in contacts:
                print(f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}")
        else:
            print("No contacts available.")
            
# Interaction with user
def main():
    manager = ContactManager()
    while True:
        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email (optional): ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            contact_id = int(input("Enter contact ID to view: "))
            manager.view_contact(contact_id)
        elif choice == '3':
            contact_id = int(input("Enter contact ID to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            manager.update_contact(contact_id, name if name else None, phone if phone else None, email if email else None)
        elif choice == '4':
            contact_id = int(input("Enter contact ID to delete: "))
            manager.delete_contact(contact_id)
        elif choice == '5':
            query = input("Enter search query: ")
            manager.search_contacts(query)
        elif choice == '6':
            manager.list_contacts()
        elif choice == '7':
            print("Exiting the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 7.")
if __name__ == "__main__":    
    main()
    