from board import Board
from board_generator import BoardGenerator
from cell import Cell
from pprint import pprint

from config.config_loader import ConfigLoader
from config.json_config_parser import JSONConfigParser
from IO.console_input import ConsoleInput

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

CONFIG_FILE_PATH = 'config.json'

config_parser = JSONConfigParser()
config_loader = ConfigLoader(CONFIG_FILE_PATH, config_parser)
pprint(config_loader.load_config())
i = ConsoleInput()