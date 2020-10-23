class Room:
    def __init__(self, number):
        self.number = number
        self.playlist = []

    def add_song_to_playlist(self, song):
        self.playlist.append(song)
