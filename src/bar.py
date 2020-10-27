class Bar:
    def __init__(self, name, entry_fee, till):
        self.name = name
        self.entry_fee = entry_fee
        self.music_library = []
        self.queue = []
        self.till = till
        self.drinks = []
        self.rooms = []

    def add_guest_to_queue(self, guest):
        self.queue.append(guest)

    def charge_guest(self, price):
        self.till += price

    def search_music_library_by_artist(self, library, artist):

        songs_by_artist = [song for song in library if song.artist == artist]
        return songs_by_artist

    def find_drink_price_by_name(self, drinks, name):
        matching_drink_price = [drink['price']
                                for drink in drinks if drink['name'] == name]

        return matching_drink_price
