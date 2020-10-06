from math import log10

from IO.base_output import BaseOutput
from board import Board
from cell import EMPTY


class ConsoleOutput(BaseOutput):
    """Outputs to the console."""

    def output(self, out: str) -> None:
        print(out)

    def output_board(self, board_obj: Board) -> None:
        board = board_obj.board
        spacing_columns = int(log10(len(board[0]))) + 2
        spacing_rows = int(log10(len(board))) + 2
        print(' ' * (spacing_rows + 2), end='')
        print(''.join(f'%{spacing_columns}s' % (column + 1) for column in range(len(board[0]))))
        print(' ' * (spacing_rows + 2), end='')
        print('-' * spacing_columns * len(board[0]))
        for index, row in enumerate(board):
            row_str = ''
            for cell in row:
                row_str += f'%{spacing_rows}s' % ('M' if cell.marked else
                                                  '#' if not cell.opened else
                                                  cell.value if cell.value != EMPTY else '_')
            print(f'%{spacing_rows}s |%s' % (index + 1, row_str))
        print()
