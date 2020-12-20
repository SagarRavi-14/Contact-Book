# from __future__ import unicode_literals
# from django.test import TestCase
# from django.contrib.auth.models import User
# from contactbook.models import Contact
# from contactbook.forms import contactbookForm
# from django.core.urlresolvers import reverse
# Create your tests here.

# class ContactTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username="user_test", password="password_test")

#     def setup(self):
#         obj1= Contact.objects.create(first_name="Mohan",last_name="Arya",email="mohan@arya.com",user_id=self.user)
    #     print(obj1)
    # def test_contact_form(self):
    #     form_data = {
    #         'first_name': 'Test firstname',
    #         'last_name': 'Test lastname',
    #         'email': 'test@test.fr',
    #     }
    #     form = contactbookForm(data=form_data)
    #     self.assertEqual(form.is_valid(), True)   
    # def test_contact_create(self):
    #     """Create a contact"""
    #     contact = Contact.objects.create(first_name="Mohan",last_name="Arya",email="mohan@arya.com",user_id=self.user)
    #     self.assertIsNotNone(contact)
    #     self.assertEquals(str(contact), "first_name last_name email user_id")
        # self.assertEquals(unicode(contact), "Test firstname Test lastname")  
        
    # def test_contact_test(self):
    #     obj1 = Contact.objects.get(first_name='Mohan',last_name="Arya",email="mohan@arya.com",user_id=user)
    #     self.assertEqual(obj1.first_name,'Mohan')
        