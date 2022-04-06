"""
    @Author: Mayank Anand
    @Date: 2022-04-05
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-06
    @Title : Testing ability to Check First and Last Name of Contact in Address Book Program
"""
import unittest as ut
from contacts import Contact


contact_instance = Contact()

class TestCheckName(ut.TestCase):
    def test_check_name(self):
        # Checking correct input
        self.assertEqual(contact_instance.check_name("Mayank", "Anand"), True)
        # Checking other correct input.
        self.assertEqual(contact_instance.check_name("", "Anand"), False)
        # Checking if parameter as integer can be accepted.
        self.assertEqual(contact_instance.check_name(11, "Anand"), True)

if __name__ == "__main__":
    ut.main()