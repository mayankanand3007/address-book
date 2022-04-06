"""
    @Author: Mayank Anand
    @Date: 2022-04-01
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-06
    @Title : Ability to add, edit and delete Contact in Address Book Program
"""
class Contact:
    def __init__(self):
        self.contacts = [{'f_name': 'Mayank', 'l_name': 'Anand','address': 'B8, Acharya Niketan', 'city': 'Mayur Vihar Phase 1', 
        'state': 'Delhi', 'zip': 110091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'},
        {'f_name': 11, 'l_name': 'Anand','address': 'B8, Acharya Niketan', 'city': 'Mayur Vihar Phase 1', 
        'state': 'Delhi', 'zip': 110091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'}]
    
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
            Dictionary of the Contact added with key value pair of the Person details.
        """
        if type(phone_no) != int:
            raise TypeError("The Phone Number can only be a number.")
        if type(zip_code) != int:
            raise TypeError("The Zip Code can only be a number.")
        self.contacts.append({'f_name': f_name, 'l_name': l_name, 
        'city': city, 'state': state, 'address': address, 'zip': zip_code, 'phone_no': phone_no, 'email': email})
        return {'f_name': f_name, 'l_name': l_name, 
        'city': city, 'state': state, 'address': address, 'zip': zip_code, 'phone_no': phone_no, 'email': email}
    
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
            Dictionary of the Contact edited with key value pair of the Person details.
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
        return {'f_name': f_name, 'l_name': l_name, 
        'city': city, 'state': state, 'address': address, 'zip': zip_code, 'phone_no': phone_no, 'email': email}

    def delete_contact_fname(self, f_name):
        """
        Description:
            Deletes Contact in Address Book using given First Name.
        Parameter:
            f_name: First name of the Person to be used to fetch Contact.
        Return:
            First Name value of Contact which is deleted from Address Book.
        """
        contacts = self.contacts
        for contact in contacts:
            if contact["f_name"] == f_name:
                contacts.remove(contact)
        return f_name