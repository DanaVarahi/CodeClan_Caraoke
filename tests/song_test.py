import unittest
from src.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song('We will Rock you', 'Queen')

    def test_song_has_a_title(self):
        self.assertEqual('We will Rock you', self.song.title)

    def test_song_has_an_artist(self):
        self.assertEqual('Queen', self.song.artist)
