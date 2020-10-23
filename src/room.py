class Room:
    def __init__(self, number):
        self.number = number
        self.playlist = []
        self.guests = []

    def add_song_to_playlist(self, song):
        self.playlist.append(song)

    def check_in_guest_to_room(self, guest):
        self.guests.append(guest)
