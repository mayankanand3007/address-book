"""
    @Author: Mayank Anand
    @Date: 2022-04-01
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-07
    @Title : Displaying Welcome, Adding, Editing and Deleting Contact to Address Book Program
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
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    address = input("Enter your address: ")
    city = input("Enter your city: ")
    state = input("Enter your state: ")
    zip_code = int(input("Enter your zip code: "))
    phone_no = int(input("Enter your phone number: "))
    email = input("Enter your email address: ")
    contact_instance.add_contact(f_name, l_name, address, city, state, zip_code, phone_no, email)
    return f"{f_name} Contact added"


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
    city = input("Enter city: ")
    state = input("Enter state: ")
    zip_code = int(input("Enter zip code: "))
    phone_no = int(input("Enter phone number: "))
    email = input("Enter email address: ")
    contact_instance.edit_contact_fname(f_name, l_name, address, city, state, zip_code, phone_no, email)
    return f"{f_name} Contact edited"


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
    contact_list = ""
    count = 1
    for contact in contacts:
        contact_list += f"Contact {count}\nFirst Name: {contact['f_name']}, " \
            f"Last Name: {contact['l_name']}, Address: {contact['address']}, State: {contact['state']}, " \
                f"Zip Code: {contact['zip_code']}, \nPhone No. {contact['phone_no']} and Email: {contact['email']}\n"
        count += 1
    return contact_list


def main():
    while True:
        print("Welcome to Address Book Program")
        print_stmts = ["Add Contact", "Edit Contact", "Delete Contact", "Display all contacts"]
        for print_stmt in range(len(print_stmts)):
            print(f"{print_stmt+1} - {print_stmts[print_stmt]}")
        # Asks user for input from the above options.
        operation_number = int(input("Enter the above number(1-4) to do the following operation: "))
        switcher = {
            1: add_contact_inputs,
            2: edit_contact_inputs,
            3: delete_contact_inputs,
            4: view_contacts,
        }
        # Checks if input given by the user is between 1 and 2 else asks the input again.
        if 0 < operation_number <= 4:
            print(switcher.get(operation_number)())
        else:
            print("Invalid number entered. Please try again: ")
            continue
        # Checks if user wants to end the loop of performing operations in Phone Book.
        if input('Do you want to check your Address Book again?(y/n): ') != 'y':
            break

if __name__ == "__main__":
    main()