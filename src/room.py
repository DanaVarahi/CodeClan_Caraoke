class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.playlist = []
        self.guests = []
        self.capacity = capacity
        self.tab = 0

    def add_song_to_playlist(self, song):
        self.playlist.append(song)

    def check_in_guest_to_room(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
        else:
            return 'Room is full.'

    def check_out_guest_from_room(self, guest):
        if len(self.guests) > 0:
            self.guests.remove(guest)

    def put_fee_on_tab(self, fee):
        self.tab += fee
