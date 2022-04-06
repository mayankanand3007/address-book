"""
    @Author: Mayank Anand
    @Date: 2022-04-05
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-05
    @Title : Testing ability to Add Contact in Address Book Program
"""
import unittest as ut
from contacts import Contact


contact_instance = Contact()

class TestSearchContacts(ut.TestCase):
    def test_search_contact(self):
        # Checking correct input for city.
        self.assertEqual(contact_instance.search_contact(True, "Mayur Vihar Phase 1"), 
        {"default": [{'f_name': 'Mayank', 'l_name': 'Anand','address': 'B8, Acharya Niketan', 
        'city': 'Mayur Vihar Phase 1', 'state': 'Delhi', 'zip': 110091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'}],
        "book1": [{'f_name': 'Mayank', 'l_name': 'Anand','address': 'B8, Acharya Niketan', 
        'city': 'Mayur Vihar Phase 1', 'state': 'HP', 'zip': 110091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'}]})
        # Checking correct input for state.
        self.assertNotEqual(contact_instance.search_contact(False, "Delhi"), 
        {"default": [{'f_name': 'Mayank', 'l_name': 'Anand','address': 'B8, Acharya Niketan', 
        'city': 'Mayur Vihar Phase 1', 'state': 'Delhi', 'zip': 110091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'},
        {'f_name': 11, 'l_name': 'Anand','address': 'B8, Acharya Niketan', 'city': 'Mayur Vihar', 
        'state': 'Delhi', 'zip': 110091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'}]})

    def test_types(self):
        # Checking if zip code is not numeric.
        self.assertRaises(TypeError, contact_instance.search_contact, "False", "Delhi")
        # Checking if phone number is not numeric.
        self.assertRaises(TypeError, contact_instance.search_contact, "True", "Mayur Vihar Phase 1")

if __name__ == "__main__":
    ut.main()