"""
    @Author: Mayank Anand
    @Date: 2022-04-01
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-01
    @Title : Displaying Welcome to Address Book Program and Adding Person to Address Book
"""
from contacts import Contact

contact_instance = Contact()

def add_contact_inputs():
    print("Enter person details to add to Address Book.")
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    address = input("Enter your address: ")
    state = input("Enter your state: ")
    zip_code = input("Enter your zip code: ")
    phone_no = input("Enter your phone number: ")
    email = input("Enter your email address: ")
    contact_instance.add_contact(f_name, l_name, address, state, zip_code, phone_no, email)
    return f_name


def main():
    while True:
        print("Welcome to Address Book Program")
        print_stmts = ["Add Contact"]
        for print_stmt in range(len(print_stmts)):
            print(f"{print_stmt+1} - {print_stmts[print_stmt]}")
        # Asks user for input from the above options.
        operation_number = int(input("Enter the above number(1) to do the following operation: "))
        print(f"{add_contact_inputs()} Contact adeed")
        # Checks if user wants to end the loop of performing operations in Phone Book.
        if input('Do you want to check your Address Book again?(y/n): ') != 'y':
            break

if __name__ == "__main__":
    main()
