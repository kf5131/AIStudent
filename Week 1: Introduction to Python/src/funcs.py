# List of contacts. Each contact is a dictionary with keys 'name', 'phone_number', and 'email'
contacts = []

def add_contact(name: str, phone_number: str, email: str) -> int:
    contacts.append({"name": name, "phone_number": phone_number, "email": email})
    # contact_id is the index of the contact in the contacts list
    return len(contacts) - 1

def update_contact(id: int, name: str, phone_number: str, email: str) -> None:
    contacts[id] = {"name": name, "phone_number": phone_number, "email": email}

def display_contacts():
    print("\nContact List:")
    print("-" * 50)
    for i, contact in enumerate(contacts):
        print(f"Contact ID: {i}")
        print(f"Name:         {contact['name']}")
        print(f"Phone Number: {contact['phone_number']}")
        print(f"Email:        {contact['email']}")
        print("-" * 50)

contact_id = add_contact("John Doe", "123-456-7890", "john@example.com")
_ = add_contact("Alice Smith", "123-456-7777", "alice@example.com")
update_contact(
    id=contact_id,
    name="John Doe",
    phone_number="555-555-5555",
    email="john@example.com"
)
display_contacts()