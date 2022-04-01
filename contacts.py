"""
    @Author: Mayank Anand
    @Date: 2022=04-01
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022=04-01
    @Title : Ability to add Contact in Address Book Program
"""
class Contact:
    def __init__(self):
        self.contacts = []

    def add_contact(self, f_name, l_name, address, state, zip, phone_no, email):
        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.state = state
        self.zip = zip
        self.phone_no = phone_no
        self.email = email
        self.contacts.append({'f_name': f_name, 'l_name': l_name,'state': state, 'zip': zip, 'phone_no': phone_no, 'email': email})