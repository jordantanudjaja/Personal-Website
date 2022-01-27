from django.test import TestCase
from ..templatetags.experience_class_tags import *
from ..models import Experience
import tempfile
import datetime

# This test file tests whether the functions in templatetags are working as intended

class TestTemplateTags(TestCase):
    def setUp(self):
        # Creating a mock Experience object
        Experience.objects.create(
            organization_name = "My Organization",
            organization_logo = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            background = "My organization is none of your business lol",
            type = "Work Experience",
            role = "CEO",
            start_date = datetime.date(2019, 3, 25),
            end_date = datetime.date(2020, 12, 10),
            tasks = "1)\ Attack and Defend\r\n22) Do Nothing\r\n3) Wolves are awesome",
            results = "14) Play Chess Mister Bankai\r\n8) Then smoke some weed"
        )

        # Getting the mocked Experience object and storing it in a variable so that it can be used in multiple tests
        self.experience_1 = Experience.objects.get(pk=1)

    def test_dict_parser(self):
        self.assertEqual(dict_parser(self.experience_1.date_parser(), 'start_month'), 'Mar')
        self.assertEqual(dict_parser(self.experience_1.date_parser(), 'start_year'), 2019)
        self.assertEqual(dict_parser(self.experience_1.date_parser(), 'end_month'), 'Dec')
        self.assertEqual(dict_parser(self.experience_1.date_parser(), 'end_year'), 2020)

    def test_list_preprocessor(self):
        self.assertEqual(list_preprocessor(self.experience_1, 'Tasks'), ['Attack and Defend', 'Do Nothing', 'Wolves are awesome'])
        self.assertEqual(list_preprocessor(self.experience_1, 'Results'), ['Play Chess Mister Bankai', 'Then smoke some weed'])
