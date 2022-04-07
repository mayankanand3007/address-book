"""
    @Author: Mayank Anand
    @Date: 2022-04-06
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-06
    @Title : Testing ability to Search Contacts by City/State in Address Book Program
"""
import unittest as ut
from contacts import Contact


contact_instance = Contact()

class TestSearchContacts(ut.TestCase):
    def test_search_contact(self):
        # Checking correct input for city.
        self.assertEqual(len(contact_instance.search_contact(True, "Mayur Vihar Phase 1").values()), 2)
        # Checking correct input for state.
        self.assertEqual(len(contact_instance.search_contact(False, "Delhi").values()), 2)
        # Checking not correct values for city.
        self.assertNotEqual(len(contact_instance.search_contact(True, "Delhi").values()), 1)
        # Checking not correct values for state.
        self.assertNotEqual(len(contact_instance.search_contact(False, "Mayur Vihar Phase 1").values()), 1)

    def test_types(self):
        # Checking if First Parameter is not Boolean.
        self.assertRaises(TypeError, contact_instance.search_contact, "False", "Delhi")
        # Checking if other First Parameter is not Boolean.
        self.assertRaises(TypeError, contact_instance.search_contact, "True", "Mayur Vihar Phase 1")

if __name__ == "__main__":
    ut.main()