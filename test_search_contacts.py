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
        self.assertEqual(len(contact_instance.search_contact(True, "Mayur Vihar Phase 1").values()), 2)
        # Checking correct input for state.
        self.assertEqual(len(contact_instance.search_contact(False, "Delhi").values()), 2)
        # Checking not correct values for city.
        self.assertNotEqual(len(contact_instance.search_contact(True, "Delhi").values()), 1)
        # Checking not correct values for state.
        self.assertNotEqual(len(contact_instance.search_contact(False, "Mayur Vihar Phase 1").values()), 1)

    def test_types(self):
        # Checking if zip code is not numeric.
        self.assertRaises(TypeError, contact_instance.search_contact, "False", "Delhi")
        # Checking if phone number is not numeric.
        self.assertRaises(TypeError, contact_instance.search_contact, "True", "Mayur Vihar Phase 1")

if __name__ == "__main__":
    ut.main()