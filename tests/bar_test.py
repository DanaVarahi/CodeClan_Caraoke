import unittest
from src.bar import Bar


class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar('Code Clan Karaoke', 100, 1000)

    def test_bar_has_name(self):
        self.assertEqual('Code Clan Karaoke', self.bar.name)

    def test_has_entry_fee(self):
        self.assertEqual(100, self.bar.entry_fee)

    def test_bar_has_till(self):
        self.assertEqual(1000, self.bar.till)
