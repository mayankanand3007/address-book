"""
    @Author: Mayank Anand
    @Date: 2022-04-01
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-05
    @Title : Ability to add and edit Contact in Address Book Program
"""
class Contact:
    def __init__(self):
        self.contacts = [{'f_name': 'Mayank', 'l_name': 'Anand','address': 'B8, Acharya Niketan', 'city': 'Mayur Vihar Phase 1', 
        'state': 'Delhi', 'zip_code': 110091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'},
        {'f_name': 'Mayank', 'l_name': 'Anand', 'address': '301, Pocket 5, Mayur Vihar Phase 1', 'city': 'New Delhi', 
        'state': 'Delhi', 'zip_code': 110091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'}]
    
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

    def edit_contact_fname(self, f_name, l_name, address, city, state, zip_code, phone_no, email):
        """
        Description:
            Edits contact using first name and updates given values of Person in contact.
        Parameter:
            f_name: First name of the Person to be used to fetch Contact.
            l_name: Last name of the Person to be added as Contact.
            address: Address of the Person to be added as Contact.
            city: City of the Person to be added as Contact.
            state: State of the Person to be added as Contact.
            zip_code: Zip Code of the Person to be added as Contact.
            phone_no: Phone Number of the Person to be added as Contact.
            email: Email Address of the Person to be added as Contact.
        Return:
            Dictionary of the All Contacts after editing Person's Contact.
        """
        contacts = self.contacts
        if type(phone_no) != int:
            raise TypeError("The Phone Number can only be a number.")
        if type(zip_code) != int:
            raise TypeError("The Zip Code can only be a number.")
        for contact in range(len(contacts)):
            if contacts[contact]["f_name"] ==  f_name:
                contacts[contact]["l_name"] = l_name
                contacts[contact]["address"] = address
                contacts[contact]["city"] = city
                contacts[contact]["state"] = state
                contacts[contact]["zip_code"] = zip_code
                contacts[contact]["phone_no"] = phone_no
                contacts[contact]["email"] = email
        return {'f_name': f_name, 'l_name': l_name,'address': address, 'city': city, 
        'state': state, 'zip_code': zip_code, 'phone_no': phone_no, 'email': email}

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
