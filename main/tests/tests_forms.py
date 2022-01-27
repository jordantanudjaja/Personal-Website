from django.test import SimpleTestCase
from ..forms import ContactForm

# This test file tests whether the form's functionality works with valid data, whether
# it does not work with both invalid data, and no data when the form is submitted.
# The tests here simulate the submission of the forms with whatever data is inputted into it.

class TestForms(SimpleTestCase):
    def test_ContactForm_valid_data(self):
        form = ContactForm(data={
            'name': 'Jordan',
            'email': 'jordo@gmail.com',
            'message': 'I am awesome'
        })

        self.assertTrue(form.is_valid())

    def test_ContactForm_invalid_data(self):
        form = ContactForm(data={
            'name': 'Jordan',
            'email': 'jordo', # Invalid email
            'message': 'Hello'
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_ContactForm_no_data(self):
        form = ContactForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
