import unittest
from src.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1)
        self.new_song = 'song3'
        self.new_guest = 'guest1'

    def test_room_has_number(self):
        self.assertEqual(1, self.room.number)

    def test_room_has_a_playlist(self):
        self.assertEqual([], self.room.playlist)

    def test_add_song_to_playlist(self):
        self.room.add_song_to_playlist(self.new_song)
        self.assertEqual(['song3'], self.room.playlist)

    def test_check_in_guest_to_room(self):
        self.room.check_in_guest_to_room(self.new_guest)
        self.assertEqual(['guest1'], self.room.guests)

    def test_check_out_guest_from_room(self):
        self.room.check_in_guest_to_room(self.new_guest)
        self.room.check_out_guest_from_room(self.new_guest)
        self.assertEqual([], self.room.guests)
