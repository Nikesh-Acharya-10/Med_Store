import unittest
from src.core.inventory import load_inventory


class TestInventory(unittest.TestCase):
    def test_load_inventory(self):
        medicines = load_inventory()
        self.assertIsInstance(medicines, list)
