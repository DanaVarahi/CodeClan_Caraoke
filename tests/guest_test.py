import unittest
from src.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest('Dana', 500, 'Cosmic Woman by Christian Winter')

    def test_guest_has_name(self):
        self.assertEqual('Dana', self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(500, self.guest.wallet)

    def test_guest_pays_fee(self):
        self.guest.guest_pays_fee(50)
        self.assertEqual(450, self.guest.wallet)

    def test_guest_has_fav_song(self):
        self.assertEqual('Cosmic Woman by Christian Winter',
                         self.guest.fav_song)
