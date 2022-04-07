"""
    @Author: Mayank Anand
    @Date: 2022-04-05
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-06
    @Title : Testing ability to Show Available Address Books in Address Book Program
"""
import unittest as ut
from contacts import Contact


contact_instance = Contact()

class TestAvailableAddressBooks(ut.TestCase):
    def test_available_address_books(self):
        # Checking correct output
        self.assertEqual(contact_instance.view_address_books(), ["default"])
        # Checking incorrect output
        self.assertNotEqual(contact_instance.view_address_books(), [""])

if __name__ == "__main__":
    ut.main()