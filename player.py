class Player:
    """Stores player score and Symbol"""
    def __init__(self, symbol):
        self.symbol = symbol

    def take_turn(self):
        position = int(input(f"Player {self.symbol}'s turn, where would you like to go?\n"))
        return position


