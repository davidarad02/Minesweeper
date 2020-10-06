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
                deltas = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
                add_delta = lambda position, delta: (position[0] + delta[0], position[1] + delta[1])
                for delta in deltas:
                    new_x, new_y = add_delta((x, y), delta)
                    if 0 <= new_y < len(board) and 0 <= new_x < len(board[new_y]):
                        board[new_y][new_x] += 1
        cell_board = [[Cell(val) for val in line] for line in board]
        return Board(cell_board)
