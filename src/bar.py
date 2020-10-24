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
