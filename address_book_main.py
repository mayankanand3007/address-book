"""
    @Author: Mayank Anand
    @Date: 2022-04-01
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-06
    @Title : Displaying Welcome, Opertions on Contact, Adding and Changing Address Book to Address Book Program
"""
from contacts import Contact

contact_instance = Contact()

def add_contact_inputs():
    """
    Description:
        Takes user input to add contact details of person in address book.
    Parameter:
        None
    Return:
        First Name of Contact added.
    """
    print("Enter person details to add to Address Book.")
    while True:
        f_name = input("Enter your first name: ")
        l_name = input("Enter your last name: ")
        if not contact_instance.check_name(f_name, l_name):
            break
        print("Please enter person details again which are not already there in Address Book.")
    address = input("Enter your address: ")
    city = input("Enter your city: ")
    state = input("Enter your state: ")
    zip_code = int(input("Enter your zip code: "))
    phone_no = int(input("Enter your phone number: "))
    email = input("Enter your email address: ")
    contact_instance.add_contact(f_name, l_name, address, city, state, zip_code, phone_no, email)
    return f"{f_name} Contact added."


def add_multiple_contact_inputs():
    """
    Description:
        Takes user input to add multiple contact details of person in address book.
    Parameter:
        None
    Return:
        List of First Name of Contact added.
    """
    no_of_contacts = int(input("Enter number of contacts to be added in Address Book: "))
    contact_names = []
    for input_contact in range(no_of_contacts):
        f_name_message = add_contact_inputs()
        # Appending First Name from the message resturned in add contact function.
        contact_names.append(f_name_message.split(" ")[0])
    return f"{contact_names} Contacts added."


def edit_contact_inputs():
    """
    Description:
        Takes user input to edit contact details of person in address book.
    Parameter:
        None
    Return:
        First Name of Contact edited.
    """
    f_name = input("Enter first name of the person you want to edit in Address Book: ")
    l_name = input("Enter last name: ")
    address = input("Enter address: ")
    state = input("Enter state: ")
    zip_code = input("Enter zip code: ")
    phone_no = input("Enter phone number: ")
    email = input("Enter email address: ")
    contact_instance.edit_contact_fname(f_name, l_name, address, state, zip_code, phone_no, email)
    return f"{f_name} Contact edited."


def delete_contact_inputs():
    """
    Description:
        Takes user input to delete contact details of person in address book.
    Parameter:
        None
    Return:
        First Name of Contact deleted.
    """
    f_name = input("Enter first name of the person you want to delete in Address Book: ")
    contact_instance.delete_contact_fname(f_name)
    return f"{f_name} Contact deleted."


def view_contacts():
    """
    Description:
        Displays all contacts in the address book.
    Parameter:
        None
    Return:
        String containing all contacts in the address book.
    """
    contacts = contact_instance.view_contacts()
    return print_contact_list(contacts)

def search_contact():
    """
    Description:
        Displays contacts searched by city/state in the address book.
    Parameter:
        None
    Return:
        String containing contacts searched by city/state in the address book.
    """
    city_state = int(input("Enter 1 if you want to search Contact by City and 2 if you want to search by State: "))
    if city_state == 1:
        query = input("Enter City by which you want to search contact in Address Book: ")
        searched_contacts = contact_instance.search_contact(True, query)
    else:
        query = input("Enter State by which you want to search contact in Address Book: ")
        searched_contacts = contact_instance.search_contact(False, query)
    return print_address_list(searched_contacts)

def view_contacts_city_state():
    """
    Description:
        Displays contacts by City/State as Key and other contact details as values.
    Parameter:
        None.
    Return:
        String of contact lists having key as city/state.
    """
    city_state = int(input("Enter 1 if you want to view Contacts by City and 2 if you want to view by State: "))
    city_state = True if city_state == 1 else False
    contacts = {}
    if city_state:
        cities = contact_instance.view_city_state(True)
        for city in cities:
            contacts[city] = []
            contacts[city].extend(contact_instance.search_contact(True, city))
    else:
        states = contact_instance.view_city_state(False)
        for state in states:
            contacts[state] = []
            contacts[state].extend(contact_instance.search_contact(False, state))
    return print_contact_list_city_state(contacts, city_state)

def view_city_state_count():
    """
    Description:
        Displays count by City/State in the current address book.
    Parameter:
        None.
    Return:
        String containing count of cities/states in current address book.
    """
    city_state = int(input("Enter 1 if you want to view Contacts by City and 2 if you want to view by State: "))
    city_state = True if city_state == 1 else False
    if city_state:
        cities = contact_instance.view_city_state(True)
        count = len(cities)
        return f"Count of Cities: {count}"
    else:
        states = contact_instance.view_city_state(False)
        count = len(states)
        return f"Count of States: {count}"

def view_sorted_name_contacts():
    """
    Description:
        Displays count by City/State in the current address book.
    Parameter:
        None.
    Return:
        String containing count of cities/states in current address book.
    """
    sorted_contacts = contact_instance.view_sorted_contacts_name()
    return print_contact_list(sorted_contacts)


def print_contact_list_city_state(searched_contacts, city_state_bool):
    """
    Description:
        Returns string converted from given Dictionary of City/State as key and their contact lists value pairs.
    Parameter:
        searched_contacts: given dictionary with address book key having contact values to be converted to string.
        city_state_bool: True if cities are to be fetched and False if states are to be fetched.
    Return:
        String with Readable City/State as key containing Contact List values for the user.
    """
    contact_list = ""
    count = 1
    for city_state in searched_contacts:
        if city_state_bool:
            contact_list += f"City {city_state}\n"
            for contact in searched_contacts[city_state]:
                contact_list += f"Contact {count}: First Name: {contact['f_name']}, Last Name: {contact['l_name']}, " \
                f"Address: {contact['address']}, State: {contact['state']}, " \
                f"Zip Code: {contact['zip']}, Phone No. {contact['phone_no']} and Email: {contact['email']}\n"
                count += 1
        else:
            contact_list += f"State {city_state}\n"
            for contact in searched_contacts[city_state]:
                contact_list += f"Contact {count}: First Name: {contact['f_name']}, Last Name: {contact['l_name']}, " \
                f"Address: {contact['address']}, City: {contact['city']}, " \
                f"Zip Code: {contact['zip']}, Phone No. {contact['phone_no']} and Email: {contact['email']}\n"
                count += 1
    return contact_list

def print_contact_list(contacts):
    """
    Description:
        Returns string converted from given contact list.
    Parameter:
        contacts: given contacts to be converted to string.
    Return:
        String with Readable Contact List values for the user.
    """
    contact_list = ""
    count = 1
    for contact in contacts:
        contact_list += f"Contact {count}\nFirst Name: {contact['f_name']}, Last Name: {contact['l_name']}, " \
            f"Address: {contact['address']}, City: {contact['city']}, State: {contact['state']}, " \
                f"Zip Code: {contact['zip']}, Phone No. {contact['phone_no']} and Email: {contact['email']}\n"
        count += 1
    return contact_list

def print_address_list(address_list_contacts):
    """
    Description:
        Returns string converted from given Dictionary of Address Book and their contact lists value pairs.
    Parameter:
        address_list_contacts: given dictionary with address book key having contact values to be converted to string.
    Return:
        String with Readable Address Book containing Contact List values for the user.
    """
    output_list = ""
    count = 1
    for address_book in address_list_contacts.keys():
        output_list += f"\nAddress Book: {address_book}\n"
        for contact in address_list_contacts[address_book]:
            output_list += f"Contact {count}: First Name: {contact['f_name']}, Last Name: {contact['l_name']}, " \
                f"Address: {contact['address']}, City: {contact['city']}, State: {contact['state']}, " \
                    f"Zip Code: {contact['zip']}, Phone No. {contact['phone_no']} and Email: {contact['email']}\n"
            count += 1
    return output_list


def add_address_book():
    """
    Description:
        Adds a separate address book to the address book data.
    Parameter:
        None
    Return:
        Name of address book added.
    """
    address_book = input("Enter name of the Address Book you want to add: ")
    contact_instance.add_address_book(address_book)
    return f"{address_book} Address Book added."


def change_address_book():
    """
    Description:
        Changes current address book to operate contacts on.
    Parameter:
        None
    Return:
        Name of address book changed to.
    """

    print("Avaiable Address Book Instances: ")
    for address_books in contact_instance.view_address_books():
        print(address_books)
    address_book = input("Enter name of the Address Book you want to change to: ")
    contact_instance.change_address_book(address_book)
    return f"{address_book} Address Book updated."


def main():
    while True:
        print("Welcome to Address Book Program")
        print_stmts = ["Add Contact", "Add Multiple Contacts", "Edit Contact", "Delete Contact", 
            "Display all Contacts", "Display Contacts by City/State", "Display Count of City or State Contacts",
            "Display Sorted Contacts by First Name and Last Name", "Search Contact by City/State", 
            "Add Address Book", "Change Address Book"]
        for print_stmt in range(len(print_stmts)):
            print(f"{print_stmt + 1} - {print_stmts[print_stmt]}")
        # Asks user for input from the above options.
        operation_number = int(input("Enter the above number(1-7) to do the following operation: "))
        switcher = {
            1: add_contact_inputs,
            2: add_multiple_contact_inputs,
            3: edit_contact_inputs,
            4: delete_contact_inputs,
            5: view_contacts,
            6: view_contacts_city_state,
            7: view_city_state_count,
            8: view_sorted_name_contacts,
            9: search_contact,
            10: add_address_book,
            11: change_address_book
        }
        # Checks if input given by the user is between 1 and 4 else asks the input again.
        if 0 < operation_number <= 10:
            print(switcher.get(operation_number)())
        else:
            print("Invalid number entered. Please try again: ")
            continue
        # Checks if user wants to end the loop of performing operations in Phone Book.
        if input('Do you want to check your Address Book again?(y/n): ') != 'y':
            break

if __name__ == "__main__":
    main()