import unittest
from src.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1)
        self.playlist = []
        self.new_song = 'song3'

    def test_room_has_number(self):
        self.assertEqual(1, self.room.number)

    def test_room_has_a_playlist(self):
        self.assertEqual([], self.room.playlist)

    # def test_add_song_to_playlist(self):
    #     self.room.playlist.add_song_to_playlist(self.new_song)
    #     self.assertEqual(['song1', 'song2', 'song3'], self.room.playlist)
