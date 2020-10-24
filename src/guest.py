class Guest:
    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song

    def guest_pays_fee(self, fee):
        self.wallet -= fee

    def guest_cheers_fav_song(self, playlist):
        for song in playlist:
            if song == self.fav_song:
                return 'Whoo!'
