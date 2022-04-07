"""
    @Author: Mayank Anand
    @Date: 2022-04-05
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-07
    @Title : Testing ability to Delete Contact in Address Book Program
"""
import unittest as ut
from contacts import Contact


contact_instance = Contact()

class TestDeleteContact(ut.TestCase):
    def test_delete_contact(self):
        # Checking correct input.
        self.assertEqual(len(contact_instance.contacts[contact_instance.current_address_book]) - 1, 
        len(contact_instance.delete_contact_fname("Mayank")))
    
    def test_types(self):
        # Checking if first name accepts numeric input.
        self.assertRaises(TypeError, contact_instance.delete_contact_fname, 123)
        # Checking if first name accepts boolean True input.
        self.assertRaises(TypeError, contact_instance.delete_contact_fname, True)
        # Checking if first name accepts boolean False input.
        self.assertRaises(TypeError, contact_instance.delete_contact_fname, False)
        # Checking if first name accepts float input.
        self.assertRaises(TypeError, contact_instance.delete_contact_fname, 21.21)
        # Checking if first name accepts complex input.
        self.assertRaises(TypeError, contact_instance.delete_contact_fname, 21.21j)


if __name__ == "__main__":
    ut.main()