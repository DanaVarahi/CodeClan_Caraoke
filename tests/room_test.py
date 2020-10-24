import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, 6)
        self.new_song = Song('The Wizard', 'Black Sabbath')
        self.new_guest = Guest('Toni', 600, Song(
            'Fear of the Dark', 'Iron Maiden'))

    def test_room_has_number(self):
        self.assertEqual(1, self.room.number)

    def test_room_has_a_playlist(self):
        self.assertEqual([], self.room.playlist)

    def test_add_song_to_playlist(self):
        self.room.add_song_to_playlist(self.new_song)
        self.assertEqual([self.new_song], self.room.playlist)

    def test_check_in_guest_to_room(self):
        self.room.check_in_guest_to_room(self.new_guest)
        self.assertEqual([self.new_guest], self.room.guests)

    def test_check_out_guest_from_room(self):
        self.room.check_in_guest_to_room(self.new_guest)
        self.room.check_out_guest_from_room(self.new_guest)
        self.assertEqual([], self.room.guests)

    def test_check_out_guest_from_empty_room(self):
        self.room.check_out_guest_from_room(self.new_guest)
        self.assertEqual([], self.room.guests)

    def test_check_in_guest_to_room_full_capacity(self):
        self.room.guests = ['guest1', 'guest2',
                            'guest3', 'guest4', 'guest5', 'guest6']
        self.assertEqual(
            'Room is full.', self.room.check_in_guest_to_room(self.new_guest))

    def test_put_fee_on_tab(self):
        self.room.put_fee_on_tab(50)
        self.assertEqual(50, self.room.tab)
