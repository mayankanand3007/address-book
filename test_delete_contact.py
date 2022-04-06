"""
    @Author: Mayank Anand
    @Date: 2022-04-05
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-05
    @Title : Testing ability to Delete Contact in Address Book Program
"""
import unittest as ut
from contacts import Contact


contact_instance = Contact()

class TestDeleteContact(ut.TestCase):
    def test_delete_contact(self):
        # Checking correct input.
        self.assertEqual(contact_instance.delete_contact_fname("Mayank"), "Mayank")
        # Checks if input for First name is not string.
        self.assertEqual(contact_instance.delete_contact_fname(11), 11)

if __name__ == "__main__":
    ut.main()