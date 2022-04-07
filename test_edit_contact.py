"""
    @Author: Mayank Anand
    @Date: 2022-04-05
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-06
    @Title : Testing ability to Edit Contact in Address Book Program
"""
import unittest as ut
from contacts import Contact


contact_instance = Contact()

class TestEditContact(ut.TestCase):
    def test_edit_contact(self):
        # Checking correct input
        self.assertTrue(contact_instance.edit_contact_fname("Mayank", "Anand", "B8, Acharya Niketan", 
        "Mayur Vihar Phase 1", "Delhi", 110091, 9560291169, "mayankan@gmail.com") in contact_instance.contacts)
        # Checking correct input for f_name not present.
        self.assertFalse(contact_instance.edit_contact_fname("Neelesh", "Rawat", "B8, Acharya Niketan", 
        "Mayur Vihar Phase 1", "Delhi", 110091, 9560291169, "mayankan@gmail.com") in contact_instance.contacts)

    def test_types(self):
        # Checking if zip code is not numeric.
        self.assertRaises(TypeError, contact_instance.edit_contact_fname, "Mayank", "Anand", "B8, Acharya Niketan",
        "Mayur Vihar Phase 1", "Delhi", "110091", 9560291169, "mayankan@gmail.com")
        # Checking if phone number is not numeric.
        self.assertRaises(TypeError, contact_instance.edit_contact_fname, "Mayank", "Anand", "B8, Acharya Niketan",
        "Mayur Vihar Phase 1", "Delhi", 110091, "9560291169", "mayankan@gmail.com")
        # Checking if not all values are passed.
        self.assertRaises(TypeError, contact_instance.edit_contact_fname, "Mayank", "Anand", "B8, Acharya Niketan",
        "Mayur Vihar Phase 1", "Delhi", "110091", 9560291169)

if __name__ == "__main__":
    ut.main()