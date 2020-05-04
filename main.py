from typing import List, Optional, Tuple
from players import TicTacToeAI, HumanPlayer, winner, game_over

def _instructions() -> None:
    """
    Instructions to display before playing the game
    """
    print('== Tic Tac Toe Controls ==\n'
          'Enter the following number that\n'
          'corresponds to the specific position on the board\n'
          '| 1 | 2 | 3 |\n'
          '-------------\n'
          '| 4 | 5 | 6 |\n'
          '-------------\n'
          '| 7 | 8 | 9 |\n')


def _play_game() -> None:
    """
    Play a round of tic tac toe
    """
    turn_num = 0
    game_board = [[None, None, None],
                  [None, None, None],
                  [None, None, None]]

    ai_first_inpt = input("Enter if AI is playing first (Y/N): ").upper()
    while ai_first_inpt != "Y" and ai_first_inpt != "N":
        print("Invalid Input! Try again")
        ai_first_inpt = input("Enter if AI is playing first (Y/N): ").upper()
    if ai_first_inpt == "Y":
        ai_first = True
    else:
        ai_first = False

    if ai_first:
        first_plyr = TicTacToeAI("X")
        scnd_plyr = HumanPlayer("O")
    else:
        first_plyr = HumanPlayer("X")
        scnd_plyr = TicTacToeAI("O")

    while not game_over(game_board):
        if turn_num % 2 == 0:
            action = first_plyr.play_move(game_board)
            if action is not None:
                i, j = action
                game_board[i][j] = first_plyr.get_player_piece()
        else:
            action = scnd_plyr.play_move(game_board)
            if action is not None:
                i, j = action
                game_board[i][j] = scnd_plyr.get_player_piece()
        turn_num += 1

    print("===== GAME OVER =====")
    winnr = winner(game_board)
    if first_plyr.get_player_piece() == winnr:
        print(first_plyr.get_child_class_name() + " wins!")
    elif scnd_plyr.get_player_piece() == winnr:
        print(scnd_plyr.get_child_class_name() + " wins!")
    else:
        print("DRAW! Nobody wins")


if __name__ == "__main__":
    _instructions()

    # Prompt Game Start
    start = input("Press S to begin. Press Q to exit: ").upper()
    while start != "S" and start != "Q":
        print("Invalid Input! Try again")
        start = input("Press S to begin. Press Q to exit: ").upper()

    if start == "S":
        continue_ = True
    else:
        continue_ = False

    while continue_:
        _play_game()

        # Prompt to play another round
        cont = input("Press C to play another round or press Q to exit: ").upper()
        while cont != "C" and start != "Q":
            print("Invalid Input! Try again")
            start = input("Press C to play another round or press Q to exit: ").upper()

        if start == "C":
            continue_ = True
        else:
            continue_ = False


