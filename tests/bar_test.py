import unittest
from src.bar import Bar
from src.song import Song
from src.guest import Guest
from src.room import Room


class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar('Code Clan Karaoke', 100, 1000)
        self.bar.drinks = [
            {'name': 'Red Kite Ale',
             'price': 250},
            {'name': 'Talisker Whisky',
             'price': 500}
        ]
        self.bar.music_library = [Song('Closer', 'Nine Inch Nails'),
                                  Song('Crack of Doom', 'Tiger Lillies'),
                                  Song('Hunter', 'Björk'),
                                  Song('The Wizard', 'Black Sabbath'),
                                  Song('Fear of the Dark', 'Iron Maiden')]

        self.bar.rooms = [Room(1, 6), Room(2, 10), Room(3, 6)]

        self.new_guest = Guest('Andy', 500, Song(
            'Everyone I love is dead', 'Type O Negative'))

    def test_bar_has_name(self):
        self.assertEqual('Code Clan Karaoke', self.bar.name)

    def test_has_entry_fee(self):
        self.assertEqual(100, self.bar.entry_fee)

    def test_bar_has_till(self):
        self.assertEqual(1000, self.bar.till)

    def test_bar_has_queue(self):
        self.assertEqual([], self.bar.queue)

    def test_bar_has_drinks(self):
        self.assertEqual(2, len(self.bar.drinks))

    def test_bar_has_music_library(self):
        self.assertEqual(5, len(self.bar.music_library))

    def test_add_guest_to_queue(self):
        self.bar.add_guest_to_queue(self.new_guest)
        self.assertEqual(1, len(self.bar.queue))

    def test_charge_guest(self):
        self.bar.charge_guest(100)
        self.assertEqual(1100, self.bar.till)

    def test_search_music_library_by_artist(self):

        self.assertEqual('Crack of Doom', self.bar.search_music_library_by_artist(
            self.bar.music_library, 'Tiger Lillies').title)
