import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song = Song('Cosmic Woman', 'Christian Winter')
        self.song2 = Song('We will Rock you', 'Queen')
        self.guest = Guest('Dana', 500, self.song)
        self.room = Room(1, 6)
        self.room.playlist = [self.song, self.song2]

    def test_guest_has_name(self):
        self.assertEqual('Dana', self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(500, self.guest.wallet)

    def test_guest_pays_fee(self):
        self.guest.guest_pays_fee(50)
        self.assertEqual(450, self.guest.wallet)

    def test_guest_has_fav_song(self):
        self.assertEqual(self.song, self.guest.fav_song)

    def test_guest_cheers_fav_song(self):
        self.assertEqual(
            'Whoo!', self.guest.guest_cheers_fav_song(self.room.playlist))
