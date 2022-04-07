"""
    @Author: Mayank Anand
    @Date: 2022-04-06
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-07
    @Title : Testing ability to Sort Contacts by Name in Address Book Program
"""
import unittest as ut
from contacts import Contact


contact_instance = Contact()

class TestSortedContactsName(ut.TestCase):
    def test_view_sorted_contacts_name(self):
        # Checking correct input.
        self.assertEqual(contact_instance.view_sorted_contacts_name(), 
        [{'f_name': 'Mayank', 'l_name': 'Anand','address': 'B8, Acharya Niketan', 'city': 'Mayur Vihar', 
        'state': 'Delhi', 'zip_code': 110091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'},
        {'f_name': 'Mayank', 'l_name': 'Bhalla','address': 'B8, Acharya Niketan', 'city': 'Mayur Vihar Phase 1', 
        'state': 'Delhi', 'zip_code': 110091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'}])
        # Checking of List is not sorted
        self.assertNotEqual(contact_instance.view_sorted_contacts_name(),
        [{'f_name': 'Mayank', 'l_name': 'Bhalla','address': 'B8, Acharya Niketan', 'city': 'Mayur Vihar Phase 1', 
        'state': 'Delhi', 'zip_code': 110091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'},
        {'f_name': 'Mayank', 'l_name': 'Anand','address': 'B8, Acharya Niketan', 'city': 'Mayur Vihar', 
        'state': 'Delhi', 'zip_code': 110091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'}])

if __name__ == "__main__":
    ut.main()