import json
import os
from datetime import datetime

class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.contacts = json.load(f)
        else:
            self.contacts = []

    def save_contacts(self):
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f, indent=2)

    def add_contact(self, name, phone, email=None, address=None):
        contact = {
            'id': len(self.contacts) + 1,
            'name': name,
            'phone': phone,
            'email': email,
            'address': address,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.contacts.append(contact)
        self.save_contacts()
        print(f"\nContact '{name}' added successfully!")

    def view_contacts(self, detailed=False):
        if not self.contacts:
            print("\nNo contacts found!")
            return

        print("\nContact List:")
        print("=" * 60)
        for contact in self.contacts:
            if detailed:
                print(f"ID: {contact['id']}")
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email'] or 'Not provided'}")
                print(f"Address: {contact['address'] or 'Not provided'}")
                print(f"Created: {contact['created_at']}")
                print(f"Last Updated: {contact['updated_at']}")
                print("-" * 60)
            else:
                print(f"{contact['id']}. {contact['name']}: {contact['phone']}")
        print("=" * 60)

    def search_contacts(self, query):
        results = []
        query = query.lower()
        for contact in self.contacts:
            if (query in contact['name'].lower() or 
                query in contact['phone'] or
                (contact['email'] and query in contact['email'].lower())):
                results.append(contact)
        
        if not results:
            print("\nNo matching contacts found!")
            return

        print(f"\nFound {len(results)} matching contact(s):")
        print("=" * 60)
        for contact in results:
            print(f"ID: {contact['id']}")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email'] or 'Not provided'}")
            print("-" * 60)

    def update_contact(self, contact_id, name=None, phone=None, email=None, address=None):
        for contact in self.contacts:
            if contact['id'] == contact_id:
                if name:
                    contact['name'] = name
                if phone:
                    contact['phone'] = phone
                if email is not None:  # Allows setting email to empty
                    contact['email'] = email
                if address is not None:  # Allows setting address to empty
                    contact['address'] = address
                
                contact['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_contacts()
                print(f"\nContact ID {contact_id} updated successfully!")
                return
        
        print(f"\nContact ID {contact_id} not found!")

    def delete_contact(self, contact_id):
        for i, contact in enumerate(self.contacts):
            if contact['id'] == contact_id:
                deleted_name = contact['name']
                del self.contacts[i]
                self.save_contacts()
                print(f"\nContact '{deleted_name}' deleted successfully!")
                return
        
        print(f"\nContact ID {contact_id} not found!")

def get_input(prompt, required=True):
    while True:
        value = input(prompt).strip()
        if not value and required:
            print("This field is required!")
        else:
            return value if value else None

def main():
    manager = ContactManager()
    
    while True:
        print("\nContact Management System")
        print("1. Add New Contact")
        print("2. View All Contacts (Brief)")
        print("3. View All Contacts (Detailed)")
        print("4. Search Contacts")
        print("5. Update Contact")
        print("6. Delete Contact")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            print("\nAdd New Contact")
            print("-" * 30)
            name = get_input("Name: ")
            phone = get_input("Phone: ")
            email = get_input("Email (optional): ", required=False)
            address = get_input("Address (optional): ", required=False)
            manager.add_contact(name, phone, email, address)
        
        elif choice == '2':
            manager.view_contacts(detailed=False)
        
        elif choice == '3':
            manager.view_contacts(detailed=True)
        
        elif choice == '4':
            query = get_input("\nEnter name, phone, or email to search: ")
            manager.search_contacts(query)
        
        elif choice == '5':
            contact_id = int(get_input("\nEnter contact ID to update: "))
            print("\nLeave fields blank to keep current values")
            name = get_input(f"New name (optional): ", required=False)
            phone = get_input(f"New phone (optional): ", required=False)
            email = get_input(f"New email (optional): ", required=False)
            address = get_input(f"New address (optional): ", required=False)
            manager.update_contact(contact_id, name, phone, email, address)
        
        elif choice == '6':
            contact_id = int(get_input("\nEnter contact ID to delete: "))
            confirm = input(f"Are you sure you want to delete this contact? (y/n): ").lower()
            if confirm == 'y':
                manager.delete_contact(contact_id)
            else:
                print("Delete operation cancelled.")
        
        elif choice == '7':
            print("\nGoodbye!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()