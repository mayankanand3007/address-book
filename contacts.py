"""
    @Author: Mayank Anand
    @Date: 2022-04-01
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-07
    @Title : Ability to operate Contact, adding and changing Address Book in Address Book Program
"""
class Contact:
    def __init__(self):
        self.current_address_book = "default"
        self.contacts = {"default": [{'f_name': 'Mayank', 'l_name': 'Anand','address': 'B8, Acharya Niketan', 
        'city': 'Mayur Vihar Phase 1', 'state': 'Delhi', 'zip_code': 110091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'},
        {'f_name': "11", 'l_name': 'Anand','address': 'B8, Acharya Niketan', 'city': 'Mayur Vihar', 
        'state': 'Delhi', 'zip_code': 110091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'}], 
        "book1": [{'f_name': 'Mayank', 'l_name': 'Anand','address': 'B8, Acharya Niketan', 
        'city': 'Mayur Vihar Phase 1', 'state': 'HP', 'zip_code': 110091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'},
        {'f_name': 'Neelesh', 'l_name': 'Rawat','address': 'Okhla', 
        'city': 'Lucknow', 'state': 'Uttar Pradesh', 'zip_code': 20091, 'phone_no': 9868474700, 'email': 'rawat9@gmail.com'}]}
    
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
        self.contacts[self.current_address_book].append({'f_name': f_name, 'l_name': l_name, 
        'city': city, 'state': state, 'address': address, 'zip': zip_code, 'phone_no': phone_no, 'email': email})
        return self.contacts[self.current_address_book]

    def check_name(self, f_name, l_name):
        """
        Description:
            Checks Person's First and Last Name if present in current Address Book.
        Parameter:
            f_name: First Name to be checked if present in current Address Book.
            l_name: Last Name to be checked if present in current Address Book.
        Return:
            True if First Name and Last Name is Present in Current Address Book Already else False.
        """
        if type(f_name) != str:
            raise TypeError
        if type(l_name) != str:
            raise TypeError
        contacts = self.contacts[self.current_address_book]
        for contact in contacts:
            if (contact["f_name"] == f_name) and (contact["l_name"] == l_name):
                return True
        return False
    
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
        contacts = self.contacts[self.current_address_book]
        if type(phone_no) != int:
            raise TypeError("The Phone Number can only be a number.")
        if type(zip_code) != int:
            raise TypeError("The Zip Code can only be a number.")
        for contact in contacts:
            if contact["f_name"] ==  f_name:
                contact["l_name"] = l_name
                contact["address"] = address
                contact["city"] = city
                contact["state"] = state
                contact["zip_code"] = zip_code
                contact["phone_no"] = phone_no
                contact["email"] = email
        return {'f_name': f_name, 'l_name': l_name, 'address': address, 'city': city, 
        'state': state, 'zip_code': zip_code, 'phone_no': phone_no, 'email': email}

    def delete_contact_fname(self, f_name):
        """
        Description:
            Deletes Contact in Address Book using given First Name.
        Parameter:
            f_name: First name of the Person to be used to fetch Contact.
        Return:
            Dictionary of the All Contacts after deleting Person's Contact.
        """
        contacts = self.contacts[self.current_address_book]
        if type(f_name) != str:
            raise TypeError("The Phone Number can only be a string.")
        for contact in contacts:
            if contact["f_name"] == f_name:
                contacts.remove(contact)
        return contacts

    def view_contacts(self):
        """
        Description:
            Returns Contacts available in the current Address Book.
        Parameter:
            None.
        Return:
            Contacts avaiable in the current Address Book.
        """
        contacts = self.contacts[self.current_address_book]
        return contacts

    def search_contact(self, city_state, query):
        """
        Description:
            Searches the given query with city_state containing boolean values for city/state query.
        Parameter:
            city_state: True if query is to be searched in the city and False if state is to be searched.
            query: City/State value which needs to be searched by in Address Book.
        Return:
            Dictionary of Address Books containing searched contants having the same value as query.
        """
        if type(city_state) != bool:
            raise TypeError
        searched_contacts = {}
        for address_book in self.contacts.keys():
            searched_values = []
            for contact in self.contacts[address_book]:
                if city_state:
                    if contact["city"] == query:
                        searched_values.append(contact)
                else:
                    if contact["state"] == query:
                        searched_values.append(contact)
            searched_contacts[address_book] = searched_values
        return searched_contacts

    def add_address_book(self, address_book_name):
        """
        Description:
            Adds given Address Book to available Address Book list.
        Parameter:
            None.
        Return:
            None.
        """
        self.contacts[address_book_name] = []

    def change_address_book(self, address_book_name):
        """
        Description:
            Returns available Address Books.
        Parameter:
            address_book_name: Address Book name to be changed into.
        Return:
            None.
        """
        if address_book_name in self.contacts:
            self.current_address_book = address_book_name

    def view_address_books(self):
        """
        Description:
            Changes Current Address Book to passed Address Book.
        Parameter:
            None.
        Return:
            Available Address Books in the Address Book Program.
        """
        return list(self.contacts.keys())
