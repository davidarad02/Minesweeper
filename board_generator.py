from random import randint

from board import Board
from cell import BOMB_VALUE, EMPTY, Cell


class BoardGenerator:
    """Generates new boards."""

    def generate_board(self, height: int, width: int, bomb_count: int) -> Board:
        """
        Generate a new board.

        :param height: The height of the new board, in rows.
        :param width: The width of the new board, in columns.
        :param bomb_count: The number of bombs to be added to the board.
        :return:
        """
        board = [[EMPTY] * width for _ in range(height)]
        added_bombs = 0
        while added_bombs < bomb_count:
            x, y = randint(0, width - 1), randint(0, height - 1)
            if board[y][x] != BOMB_VALUE:
                board[y][x] = BOMB_VALUE
                added_bombs += 1
        cell_board = [[Cell(val) for val in line] for line in board]
        return Board(cell_board)
