from typing import List, Optional

GAME_BOARD = [[None, None, None],
              [None, None, None],
              [None, None, None]]

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

if __name__ == "__main__":
    turn_num = 0

    while True:
        pass