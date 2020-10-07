from typing import List
from copy import deepcopy

from cell import Cell, EMPTY
from errors.game_lost_error import GameLostError
from errors.game_won_error import GameWonError


class Board:
    """Represents the board of the game."""

    def __init__(self, board_array: List[List[Cell]]) -> None:
        """
        :param board_array: The board
        """
        self._board = board_array

    @property
    def board(self) -> List[List[Cell]]:
        """Get the read-only `_board` value."""
        return deepcopy(self._board)

    def open_cell(self, x: int, y: int) -> None:
        """
        Open a single cell. Check whether the game is over.

        :param x: The x-coordinate of the cell on the board.
        :param y: The y-coordinate of the cell on the board.
        """
        cell = self._board[y][x]
        if cell.opened:
            return

        cell.open()
        self._check_game_end(x, y)

        if cell.value == EMPTY:
            # Try to open all cells around the empty cell.
            deltas = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
            add_delta = lambda position, delta: (position[0] + delta[0], position[1] + delta[1])
            for delta in deltas:
                new_x, new_y = add_delta((x, y), delta)
                if 0 <= new_y < len(self._board) and 0 <= new_x < len(self._board[new_y]):
                    self.open_cell(new_x, new_y)

    def _check_game_end(self, x: int, y: int) -> None:
        """
        Test whether the game should end.

        :param x: The x-coordinate of the cell on the board.
        :param y: The y-coordinate of the cell on the board.
        :raises:
            GameLostError: If the opened cell is a bomb.
            GameWonError: If all of the non-bomb cells have been opened.
        """
        if self._board[y][x].is_bomb:
            raise GameLostError(x, y)

        bomb_count = sum(c.is_bomb for line in self._board for c in line)
        closed_cell_count = sum(not c.opened for line in self._board for c in line)
        if bomb_count == closed_cell_count:
            raise GameWonError()

    def mark_cell(self, x: int, y: int) -> None:
        """
        Mark or unmark a cell on the board as a bomb.

        :param x: The x-coordinate of the cell on the board.
        :param y: The y-coordinate of the cell on the board.
        """
        self._board[y][x].mark()
