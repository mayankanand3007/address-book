"""
    @Author: Mayank Anand
    @Date: 2022-04-06
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-07
    @Title : Testing ability to Read Contacts in Address Book Program from json file
"""
import unittest as ut
from contacts import Contact


contact_instance = Contact()

class TestReadTextContacts(ut.TestCase):
    def test_read_txt(self):
        # Checking correct input.
        self.assertEqual(contact_instance.read_json(), {'default': [{'f_name': 'Mayank', 'l_name': 'Bhalla', 
        'address': 'B8, Acharya Niketan', 'city': 'Mayur Vihar Phase 1', 'state': 'Uttar Pradesh', 
        'zip_code': 910091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'}, {'f_name': 'Mayank', 
        'l_name': 'Anand', 'address': 'B8, Acharya Niketan', 'city': 'Mayur Vihar', 'state': 'Delhi', 
        'zip_code': 210091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'}, {'f_name': 'Mayank', 
        'l_name': 'Gupta', 'address': 'B8, Acharya Niketan', 'city': 'Okhla', 'state': 'Delhi', 'zip_code': 110091, 
        'phone_no': 9560291169, 'email': 'mayankan@gmail.com'}], 'book1': [{'f_name': 'Mayank', 'l_name': 'Anand', 
        'address': 'B8, Acharya Niketan', 'city': 'Mayur Vihar Phase 1', 'state': 'HP', 'zip_code': 110091, 
        'phone_no': 9560291169, 'email': 'mayankan@gmail.com'}, {'f_name': 'Neelesh', 'l_name': 'Rawat', 
        'address': 'Okhla', 'city': 'Lucknow', 'state': 'Uttar Pradesh', 'zip_code': 20091, 'phone_no': 9868474700, 
        'email': 'rawat9@gmail.com'}]})
        # Checking incorrect values.
        self.assertNotEqual(contact_instance.read_json(), {'default': [{'f_name': 'Mayank', 'l_name': 'Bhalla', 
        'address': 'B8, Acharya Niketan', 'city': 'Mayur Vihar Phase 1', 'state': 'Uttar Pradesh', 
        'zip_code': 910091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'}, {'f_name': 'Mayank', 
        'l_name': 'Anand', 'address': 'B8, Acharya Niketan', 'city': 'Mayur Vihar', 'state': 'Delhi', 
        'zip_code': 210091, 'phone_no': 9560291169, 'email': 'mayankan@gmail.com'}, {'f_name': 'Mayank', 
        'l_name': 'Gupta', 'address': 'B8, Acharya Niketan', 'city': 'Okhla', 'state': 'Delhi', 'zip_code': 110091, 
        'phone_no': 9560291169, 'email': 'mayankan@gmail.com'}]})

if __name__ == "__main__":
    ut.main()