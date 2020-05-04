from typing import List, Optional, Tuple, Set

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

class Player:
    """An abstract class for a player for this game of tic tac toe"""

    _player: str
    _board: List[List[Optional[str]]]

    def __init__(self, player: str) -> None:
        """
        Initializes this player.

        Precondition: <player> is one of either the string 'X' or 'O'
        """
        self._player = player
        self._board = [[None, None, None],
                       [None, None, None],
                       [None, None, None]]

    def play_move(self, board: List[List[Optional[str]]]) -> Optional[Tuple[int, int]]:
        """
        Returns a valid i, j index on the current <board>
        that this player has chosen to place their move. Returns
        None if there are no possible moves.

        Precondition: <board> is exactly a 3x3 2d list
        """
        #Update this player's board
        for col in range(len(board)):
            for row in range(len(board)):
                self._board[col][row] = board[col][row]

        #Make move
        return self._choose_move()

    def get_player_piece(self) -> str:
        """
        Returns the piece representing this player on the board (i.e. X/0)
        """
        return self._player

    def _choose_move(self) -> Optional[Tuple[int, int]]:
        """
        Choose a valid  i, j index on the current board to make
        a move. Returns None if there are no possible moves.
        """
        raise NotImplementedError

    def get_child_class_name(self) -> str:
        """
        Returns the child class of player this player is (i.e. AI or Human)
        """
        raise NotImplementedError


class TicTacToeAI(Player):
    """An AI for playing tic tac toe"""

    _player: str
    _board: List[List[Optional[str]]]

    def _choose_move(self) -> Optional[Tuple[int, int]]:
        """
        Choose a valid  i, j index on the current board to make
        a move. Returns None if there are no possible moves.
        """
        print("AI Turn...")
        if self._player == "X":
            return self._max_value(self._board)[1]
        else:
            return self._min_value(self._board)[1]

    def _moves(self, board: List[List[Optional[str]]]) -> Set[Tuple[int, int]]:
        """
        Returns all possible moves (i, j) available on the <board>.

        Precondition: <board> is exactly a 3x3 2d list
        """
        possible_moves = set()

        for row_id in range(len(board)):
            row = board[row_id]
            for cell_id in range(len(row)):
                if row[cell_id] is None:
                    possible_moves.add((row_id, cell_id))

        return possible_moves

    def _result(self, board: List[List[Optional[str]]], move: Tuple[int, int]) \
            -> List[List[Optional[str]]]:
        """
        Returns the board that results from making the <move> on the <board>.

        Precondition: <board> is exactly a 3x3 2d list.
                      <move> contains only the ints 0, 1, or 2.
        """
        board_copy = [[row[k] for k in range(len(row))] for row in board]
        i, j = move
        if board_copy[i][j] is None:
            board_copy[i][j] = self._player
            return board_copy
        else:
            raise Exception("Not valid action")

    def _score(self, board: List[List[Optional[str]]]) -> int:
        """
        Returns the score for the given <board>. The score is 1 if X has won
        the game, -1 if O has won and 0 otherwise.

        Precondition: <board> is exactly a 3x3 2d list
        """
        if winner(board) == "X":
            return 1
        elif winner(board) == "O":
            return -1
        else:
            return 0

    def _max_value(self, board: List[List[Optional[str]]]) -> Tuple[int, Optional[Tuple[int, int]]]:
        """
        Returns a tuple of the optimal score and the move that results in that score
        for the max player on the <board>. If there are no possible moves, the score of
        the <board> and None is instead returned as a Tuple.

        Precondition: <board> is exactly a 3x3 2d list
        """
        if game_over(board):
            return (self._score(board), None)

        poss_moves = {-100: None}

        for action in self._moves(board):
            score = self._min_value(self._result(board, action))[0]
            poss_moves[score] = action

        optimal_score = max(poss_moves)

        return (optimal_score, poss_moves[optimal_score])

    def _min_value(self, board: List[List[Optional[str]]]) -> Tuple[int, Optional[Tuple[int, int]]]:
        """
        Returns a tuple of the optimal score and the action that results in that score
        for the min player currently on the <board>. If there are no possible moves, the score of
        the <board> and None is instead returned as a Tuple.

        Precondition: <board> is exactly a 3x3 2d list
        """
        if game_over(board):
            return (self._score(board), None)

        moves = {100: None}

        for action in self._moves(board):
            score = self._max_value(self._result(board, action))[0]
            moves[score] = action

        optimal_score = min(moves)

        return (optimal_score, moves[optimal_score])

    def get_child_class_name(self) -> str:
        """
        Returns the child class of player this player is (i.e. AI or Human)
        """
        return "Artificial Intelligence"

class HumanPlayer(Player):
    """A Human player"""

    _player: str
    _board: List[List[Optional[str]]]

    def _print_board(self) -> None:
        """
        Prints board to console for player to see.
        """
        flat_board = []
        for row in self._board:
            for item in row:
                if item is None:
                    flat_board.append(" ")
                else:
                    flat_board.append(item)
        print('==== Current Board ====')
        str_board = "\t-------------\n\t"
        for i in range(len(flat_board)):
            str_board += "| " + flat_board[i] + " "
            if i % 3 == 2:
                str_board += "|\n\t-------------\n\t"
        print(str_board)

    def _choose_move(self) -> Optional[Tuple[int, int]]:
        """
        Choose a valid  i, j index on the current board to make
        a move. Returns None if there are no possible moves.
        """
        if game_over(self._board):
            return None

        self._print_board()
        move = input("Your turn! Enter move to make: ")
        while not move.isdigit() or self._valid_num(int(move) - 1):
            print("Invalid Move! Try again")
            move = input("Enter move to make: ")

        choice = int(move) - 1
        return (choice // 3, choice % 3)

    def _valid_num(self, move: int) -> bool:
        """
        Returns true iff <move> is a valid move that can be made on
        the game board.
        """
        i, j = move // 3, move % 3
        try:
            return self._board[i][j] is not None
        except(IndexError):
            return False

    def get_child_class_name(self) -> str:
        """
        Returns the child class of player this player is (i.e. AI or Human)
        """
        return "Human (Yes, you!)"

