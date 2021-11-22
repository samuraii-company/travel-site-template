from django.test import TestCase
from .models import UserData, Subscirbe_Emails, Destinations, Blog
# Create your tests here.


class TestModels(TestCase):

    def setUp(self):
        self.userdata = UserData.objects.create(
            name="test name",
            phone_number="+7922222222",
            email="test@gmail.com")

    def test_post_model(self):
        d = self.userdata
        self.assertTrue(isinstance(d, UserData))
        self.assertEqual(str(d), "test name")
