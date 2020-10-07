from IO.console_output import ConsoleOutput
from IO.str_to_int_validator import StrToIntValidator
from board import Board
from board_generator import BoardGenerator
from cell import Cell

from config.config_loader import ConfigLoader
from config.json_config_parser import JSONConfigParser
from IO.console_input import ConsoleInput
from engine import GameEngine
from menu import Menu

b = Board([
    [Cell(-1), Cell(1), Cell(-1)],
    [Cell(1), Cell(2), Cell(1)],
    [Cell(0), Cell(0), Cell(0)],
    [Cell(1), Cell(1), Cell(1)],
    [Cell(1), Cell(-1), Cell(1)],
])

bg = BoardGenerator()
b2 = bg.generate_board(10, 50, 10)

CONFIG_FILE_PATH = 'config.json'

config_parser = JSONConfigParser()
config_loader = ConfigLoader(CONFIG_FILE_PATH, config_parser)

i = ConsoleInput()
o = ConsoleOutput()
engine = GameEngine(bg)
validator = StrToIntValidator()
menu = Menu(config_loader, engine, i, o, validator)
menu.run_main_menu()
