class GameBoard:
    def __init__(self):
        self.current_board = [" " for _ in range(9)]

    def display_board(self):
        print("""
{} | {} | {}
---------
{} | {} | {}
---------
{} | {} | {}""".format(*self.current_board))

    def update_board(self, position, symbol):
        if self.current_board[position - 1] == " ":
            self.current_board[position - 1] = symbol
            return True

        else:
            print("Spot taken, choose another.")
            return False

    def check_for_end(self):
        winning_patterns = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),    # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),    # Columns
            (0, 4, 8), (2, 4, 6)                # Diagonals
        ]
        for pattern in winning_patterns:
            if self.current_board[pattern[0]] == self.current_board[pattern[1]] == self.current_board[pattern[2]] != " ":
                return self.current_board[pattern[0]]

        if " " not in self.current_board:
            return "Draw"

        return None

