"""Liam Meisinger's Tic Tac Toe game"""

"""Imports"""
from art import logo
from player import *
from gameboard import *

def play_game():
    player_X = Player("X")
    player_O = Player("O")
    game_board = GameBoard()
    current_player = player_X
    game_on = True

    while game_on:
        print(logo)
        game_board.display_board()
        valid_move = False
        while not valid_move:
            position = current_player.take_turn()
            valid_move = game_board.update_board(position, current_player.symbol)
        result = game_board.check_for_end()
        if result:
            game_board.display_board()
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"Player {result} wins!")
            game_on = False
        else:
            current_player = player_O if current_player == player_X else player_X


while True:
    play_game()
    print(logo)
    again = input("Would you like to play again? 'Y' or 'N'\n").upper()
    if again != 'Y':
        print("Thanks for playing!")
        game_on = True

