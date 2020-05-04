from typing import List, Optional, Tuple
from players import TicTacToeAI, HumanPlayer

def winner(board: List[List[Optional[str]]]) -> Optional[str]:
    """
    Returns the winner of the game, iff one exists.

    Precondition: <board> is exactly a 3x3 2d list
    """
    for player in ["X", "O"]:
        if _row_win(player, board) or _column_win(player, board) or \
            _diagonal_win(player, board):
            return player
    return None

def _row_win(player: str, board: List[List[Optional[str]]]) -> bool:
    """
    Returns True iff the player has won by row. False otherwise.

    Precondition: <board> is exactly a 3x3 2d list
                  <player> is either the string 'X' or 'O'
    """
    for row in board:
        if row == [player] * len(board):
            return True
    return False

def _column_win(player: str, board: List[List[Optional[str]]]) -> bool:
    """
    Returns True iff the player has won by column. False otherwise.

    Precondition: <board> is exactly a 3x3 2d list
                  <player> is either the string 'X' or 'O'
    """
    for i in range(len(board)):
        col = [row[i] for row in board]
        if col == [player] * len(board):
            return True
    return False

def _diagonal_win(player: str, board: List[List[Optional[str]]]) -> bool:
    """
    Returns True iff the player has won diagonally. False otherwise.

    Precondition: <board> is exactly a 3x3 2d list
                  <player> is either the string 'X' or 'O'
    """
    lower_diag = [board[i][i] for i in range(len(board))]
    upper_diag = [board[i][-1-i] for i in range(len(board))]
    return lower_diag == [player] * len(board) or upper_diag == [player] * len(board)


def game_over(board: List[List[Optional[str]]]) -> bool:
    """
    Returns True if game is over, False otherwise.

    Precondition: <board> is exactly a 3x3 2d list
    """
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell is None:
                return False
    return True

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

def _user_setup() -> Tuple[str, str, bool]:
    """
    Returns a tuple of the player type of the first round player,
    the player type of the second player, and a boolean determining
    if the AI will be the first to make a move or not.
    """
    ai_first = input("Enter if AI is playing first (Y/N): ").upper()
    while ai_first != "Y" and ai_first != "N":
        print("Invalid Input! Try again")
        ai_first = input("Enter if AI is playing first (Y/N): ").upper()

    first_ = input("Enter the player type of player 1 (X/O): ").upper()
    while first_ != "X" and first_ != "O":
        print("Invalid Input! Try again")
        first_ = input("Enter the player type of player 1 (X/O): ").upper()

    if first_ == "X" and ai_first == "Y":
        return ("X", "O", True)
    elif first_ == "X" and ai_first == "N":
        return ("X", "O", False)
    elif first_ == "O" and ai_first == "Y":
        return ("0", "X", True)
    elif first_ == "O" and ai_first == "N":
        return ("0", "X", False)

def _play_game() -> None:
    """
    Play a round of tic tac toe
    """
    turn_num = 0
    game_board = [[None, None, None],
                  [None, None, None],
                  [None, None, None]]

    first_, second_, ai_first = _user_setup()

    if ai_first:
        first_plyr = TicTacToeAI(first_)
        scnd_plyr = HumanPlayer(second_)
    else:
        first_plyr = HumanPlayer(first_)
        scnd_plyr = TicTacToeAI(second_)

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


