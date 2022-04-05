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
        if type(phone_no) != int:
            raise TypeError("The Phone Number can only be a number.")
        if type(zip_code) != int:
            raise TypeError("The Zip Code can only be a number.")
        self.contacts.append({'f_name': f_name, 'l_name': l_name, 
        'city': city, 'state': state, 'address': address, 'zip': zip_code, 'phone_no': phone_no, 'email': email})
        return {'f_name': f_name, 'l_name': l_name, 
        'city': city, 'state': state, 'address': address, 'zip': zip_code, 'phone_no': phone_no, 'email': email}