"""
    @Author: Mayank Anand
    @Date: 2022-04-05
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-07
    @Title : Testing ability to Check First and Last Name of Contact in Address Book Program
"""
import unittest as ut
from contacts import Contact


contact_instance = Contact()

class TestCheckName(ut.TestCase):
    def test_check_name(self):
        # Checking correct input
        self.assertTrue(contact_instance.check_name("Mayank", "Anand"))
        # Checking another correct input.
        self.assertFalse(contact_instance.check_name("", "Anand"), False)

    def test_types(self):
        # Checking if first name accepts numeric input.
        self.assertRaises(TypeError, contact_instance.check_name, 123, "Anand")

if __name__ == "__main__":
    ut.main()