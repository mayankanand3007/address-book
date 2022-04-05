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

class TestAddContact(ut.TestCase):
    def test_add_contact(self):
        # Checking correct input
        self.assertEqual(contact_instance.add_contact("Mayank", "Anand", "B8, Acharya Niketan", 
        "Mayur Vihar Phase 1", "Delhi", 110091, 9560291169, "mayankan@gmail.com"), 
        {'f_name': 'Mayank', 'l_name': 'Anand','address': 'B8, Acharya Niketan', 'city': 'Mayur Vihar Phase 1', 
        'state': 'Delhi', 'zip': 110091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'})
        # Checking data types input for zip code.
        self.assertNotEqual(contact_instance.add_contact("Mayank", "Anand", "B8, Acharya Niketan", 
        "Mayur Vihar Phase 1", "Delhi", 110091, 9560291169, "mayankan@gmail.com"), 
        {'f_name': 'Mayank', 'l_name': 'Anand','address': 'B8, Acharya Niketan', 'city': 'Mayur Vihar Phase 1', 
        'state': 'Delhi', 'zip': '110091', 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'})
        # Checking data types input for phone number.
        self.assertNotEqual(contact_instance.add_contact("Mayank", "Anand", "B8, Acharya Niketan", 
        "Mayur Vihar Phase 1", "Delhi", 110091, 9560291169, "mayankan@gmail.com"), 
        {'f_name': 'Mayank', 'l_name': 'Anand','address': 'B8, Acharya Niketan', 'city': 'Mayur Vihar Phase 1', 
        'state': 'Delhi', 'zip': 110091, 'phone_no': '9560291169', 'email': 'mayankan@gmail.com'})

    def test_types(self):
        # Checking if zip code is not numeric.
        self.assertRaises(TypeError, contact_instance.add_contact, "Mayank", "Anand", "B8, Acharya Niketan",
        "Mayur Vihar Phase 1", "Delhi", "110091", 9560291169, "mayankan@gmail.com")
        # Checking if phone number is not numeric.
        self.assertRaises(TypeError, contact_instance.add_contact, "Mayank", "Anand", "B8, Acharya Niketan",
        "Mayur Vihar Phase 1", "Delhi", 110091, "9560291169", "mayankan@gmail.com")
        # Checking if not all values are passed.
        self.assertRaises(TypeError, contact_instance.add_contact, "Mayank", "Anand", "B8, Acharya Niketan",
        "Mayur Vihar Phase 1", "Delhi", "110091", 9560291169)

if __name__ == "__main__":
    ut.main()