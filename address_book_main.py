"""
    @Author: Mayank Anand
    @Date: 2022=04-01
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022=04-01
    @Title : Displaying Welcome to Address Book Program and Adding Person to Address Book
"""
from contacts import Contact


def main():
    print("Welcome to Address Book Program")
    print("Enter person details to add to Address Book.")
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    address = input("Enter your address: ")
    state = input("Enter your state: ")
    zip = input("Enter your zip code: ")
    phone_no = input("Enter your phone number: ")
    email = input("Enter your email address: ")
    Contact.add_contact(f_name, l_name, address, state, zip, phone_no, email)

if __name__ == "__main__":
    main()
