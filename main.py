from board import Board
from board_generator import BoardGenerator
from cell import Cell
from pprint import pprint

from game_lost_error import GameLostError

b = Board([
    [Cell(-1), Cell(1), Cell(-1)],
    [Cell(1), Cell(2), Cell(1)],
    [Cell(0), Cell(0), Cell(0)],
    [Cell(1), Cell(1), Cell(1)],
    [Cell(1), Cell(-1), Cell(1)],
])

bg = BoardGenerator()
b2 = bg.generate_board(3, 5, 3)
pprint(b2._board)

