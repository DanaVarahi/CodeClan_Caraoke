import unittest
from src.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest('Dana', 500)

    def test_guest_has_name(self):
        self.assertEqual('Dana', self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(500, self.guest.wallet)
