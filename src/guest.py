class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def guest_pays_fee(self, fee):
        self.wallet -= fee
