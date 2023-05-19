import unittest
from django.test import TestCase
from Home.models import models

class MyModelTestCase(TestCase):
    def setUp(self):
        models.objects.create(name='Test Model')

    def test_my_model(self):
        model = models.objects.get(name='Test Model')
        self.assertEqual(model.name, 'Test Model')


# Create your tests here.
