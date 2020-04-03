from django.test import TestCase
from .models import Item

class TestItemModel(TestCase):
    def test_done_defaults_to_failse(self):
        item = Item(name="Create a test")
        item.save()
        self.assertEqual(item.name, "Create a test")
        self.assertFalse(item.done)

    def test_can_create_an_item_with_name_and_status(self):
        item = Item (name="Create a test", done=True)
        item.save()
        self.assertEqual(item.name, "Create a test")
        self.assertTrue(item.done)

    # Test to ensure the instance of the Item object has the same name as the given
    def test__item_as_a_string(self):
        item = Item(name="Create a test")
        self.assertEqual("Create a test", str(item))