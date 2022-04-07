"""
    @Author: Mayank Anand
    @Date: 2022-04-01
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-05
    @Title : Ability to add Contact in Address Book Program
"""
class Contact:
    def __init__(self):
        self.contacts = []

    def add_contact(self, f_name, l_name, address, city, state, zip_code, phone_no, email):
        """
        Description:
            Adds contact using given values of Person to be added as contact.
        Parameter:
            f_name: First name of the Person to be added as Contact.
            l_name: Last name of the Person to be added as Contact.
            address: Address of the Person to be added as Contact.
            city: City of the Person to be added as Contact.
            state: State of the Person to be added as Contact.
            zip_code: Zip Code of the Person to be added as Contact.
            phone_no: Phone Number of the Person to be added as Contact.
            email: Email Address of the Person to be added as Contact.
        Return:
            Dictionary of the All Contacts after adding Person's Contact.
        """
        if type(phone_no) != int:
            raise TypeError("The Phone Number can only be a number.")
        if type(zip_code) != int:
            raise TypeError("The Zip Code can only be a number.")
        self.contacts.append({'f_name': f_name, 'l_name': l_name, 
        'city': city, 'state': state, 'address': address, 'zip_code': zip_code, 'phone_no': phone_no, 'email': email})
        return self.contacts

    def view_contacts(self):
        """
        Description:
            Returns Contacts available in the current Address Book.
        Parameter:
            None.
        Return:
            Contacts avaiable in the current Address Book.
        """
        contacts = self.contacts
        return contacts