"""
    @Author: Mayank Anand
    @Date: 2022-04-01
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-07
    @Title : Ability to operate Contact, adding and changing Address Book in Address Book Program
"""
import csv
import json
from email import header

class Contact:
    def __init__(self):
        self.current_address_book = "default"
        self.contacts = {}
        self.db_option = ""
    
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

    def view_sorted_contacts_name(self):
        """
        Description:
            Returns sorted Contacts by f_name and l_name available in the current Address Book.
        Parameter:
            None.
        Return:
            Sorted Contacts by f_name and l_name avaiable in the current Address Book.
        """
        contacts = self.contacts[self.current_address_book]
        sorted_contacts = sorted(contacts, key = lambda x: [x["f_name"], x["l_name"]])
        return sorted_contacts

    def view_sorted_contacts_city(self):
        """
        Description:
            Returns sorted Contacts by city available in the current Address Book.
        Parameter:
            None.
        Return:
            Sorted Contacts by city avaiable in the current Address Book.
        """
        contacts = self.contacts[self.current_address_book]
        sorted_contacts = sorted(contacts, key = lambda x: x["city"])
        return sorted_contacts

    def view_sorted_contacts_state(self):
        """
        Description:
            Returns sorted Contacts by state available in the current Address Book.
        Parameter:
            None.
        Return:
            Sorted Contacts by state avaiable in the current Address Book.
        """
        contacts = self.contacts[self.current_address_book]
        sorted_contacts = sorted(contacts, key = lambda x: x["state"])
        return sorted_contacts

    def view_sorted_contacts_zip(self):
        """
        Description:
            Returns sorted Contacts by zip code available in the current Address Book.
        Parameter:
            None.
        Return:
            Sorted Contacts by zip code avaiable in the current Address Book.
        """
        contacts = self.contacts[self.current_address_book]
        sorted_contacts = sorted(contacts, key = lambda x: x["zip_code"])
        return sorted_contacts

    def view_city_state(self, city_state):
        """
        Description:
            Returns list cities or states as list if given city_state is True/False.
        Parameter:
            city_state: True if cities are to be fetched and False if states are to be fetched.
        Return:
            List of cities/states as per given city_state boolean value.
        """
        if type(city_state) != bool:
            raise TypeError
        contacts = self.contacts[self.current_address_book]
        cities_states = []
        if city_state:
            for contact in contacts:
                if contact["city"] not in cities_states:
                    cities_states.append(contact["city"])
        else:
            for contact in contacts:
                if contact["state"] not in cities_states:
                    cities_states.append(contact["state"])
        return cities_states

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

    def search_contact_current_address_book(self, city_state, query):
        """
        Description:
            Searches the given query with city_state containing boolean values for city/state query.
        Parameter:
            city_state: True if query is to be searched in the city and False if state is to be searched.
            query: City/State value which needs to be searched by in Address Book.
        Return:
            List of searched contants having the same value as query in current address book.
        """
        if type(city_state) != bool:
            raise TypeError
        searched_contacts = []
        for contact in self.contacts[self.current_address_book]:
            if city_state:
                if contact["city"] == query:
                    searched_contacts.append(contact)
            else:
                if contact["state"] == query:
                    searched_contacts.append(contact)
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

    def write_txt(self):
        """
        Description:
            Writes contacts Dictionary containing all Address Books to Text File.
        Parameter:
            None.
        Return
            None.
        """
        with open("address_book.txt","w") as ad_book:
            ad_book.write(str(self.contacts))

    def read_txt(self):
        """
        Description:
            Reads contacts Dictionary containing all Address Books from Text File.
        Parameter:
            None.
        Return
            Contacts Dictionary containing all Address Books from Text File.
        """
        with open("address_book.txt","r") as ad_book:
            contacts = ad_book.read()
            contact_dict = eval(contacts)
            self.contacts = contact_dict
            return contact_dict

    def write_csv(self):
        """
        Description:
            Writes contacts Dictionary containing all Address Books to Separate Csv Files.
        Parameter:
            None.
        Return
            None.
        """
        contacts = self.contacts
        for address_book in contacts:
            if address_book != []:
                file_name = address_book + ".csv"
                with open(file_name, "w") as ad_book:
                    book = csv.writer(ad_book)
                    book.writerow(('f_name', 'l_name', 'address', 'city', 'state', 'zip_code', 'phone_no', 'email'))
                    for row in contacts[address_book]:
                        book.writerow((row['f_name'], row['l_name'], row['address'], row['city'], row['state'], 
                        row['zip_code'], row['phone_no'], row['email']))

    def read_csv(self, address_book):
        """
        Description:
            Reads contacts Dictionary containing given Address Book name from CSV File.
        Parameter:
            address_book: Given Address Book to be fetched from CSV File of the same name.
        Return
            Contacts Dictionary containing given Address Books from CSV File.
        """
        file_name = address_book + ".csv"
        with open(file_name, "r") as ad_book:
            contacts = [row for row in csv.DictReader(ad_book)]
            contacts_dict = {address_book : contacts}
            self.contacts[address_book] = contacts
            return contacts_dict

    def write_json(self):
        """
        Description:
            Writes contacts Dictionary containing all Address Books to Json File.
        Parameter:
            None.
        Return
            None.
        """
        with open("address_book.json", "w") as ad_book:
            json.dump(self.contacts, ad_book, indent = 4)

    def read_json(self):
        """
        Description:
            Reads contacts Dictionary containing all Address Books from Json File.
        Parameter:
            None.
        Return
            Contacts Dictionary containing all Address Books from Json File.
        """
        with open("address_book.json", "r") as ad_book:
            address_book = json.load(ad_book)
            self.contacts = address_book
            return address_book