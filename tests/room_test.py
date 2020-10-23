import unittest
from src.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, ['song1', 'song2'])

    def test_room_has_number(self):
        self.assertEqual(1, self.room.number)

    def test_room_has_a_playlist(self):
        self.assertEqual(['song1', 'song2'], self.room.playlist)
