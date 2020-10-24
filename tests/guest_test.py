import unittest
from src.guest import Guest
from src.room import Room


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest('Dana', 500, 'Cosmic Woman by Christian Winter')
        self.room = Room(1, 6)
        self.room.playlist = ['We will Rock you by Queen',
                              'Cosmic Woman by Christian Winter']

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

    def test_guest_cheers_fav_song(self):
        self.assertEqual(
            'Whoo!', self.guest.guest_cheers_fav_song(self.room.playlist))
