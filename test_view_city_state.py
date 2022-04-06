"""
    @Author: Mayank Anand
    @Date: 2022-04-06
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-06
    @Title : Testing ability to View Cities/States in Address Book Program
"""
import unittest as ut
from contacts import Contact


contact_instance = Contact()

class TestSearchContacts(ut.TestCase):
    def test_search_contact(self):
        # Checking correct input for city.
        self.assertEqual(contact_instance.view_city_state(True), 
        ['Mayur Vihar Phase 1', 'Mayur Vihar'])
        # Checking correct input for state.
        self.assertNotEqual(contact_instance.view_city_state(False), 
        ['Delhi', 'HP'])

    def test_types(self):
        # Checking if First Parameter is not Boolean.
        self.assertRaises(TypeError, contact_instance.view_city_state, "False")
        #Checking if other First Parameter is not Boolean.
        self.assertRaises(TypeError, contact_instance.view_city_state, "True")

if __name__ == "__main__":
    ut.main()