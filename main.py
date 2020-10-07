"""
Minesweeper - A game to search, mark, and clear bombs.

Rules of the game:
- You have a board of cells.
- Every cell could have a bomb.
- If you open a cell that has a bomb, you loose!
- The target of the game is to clear all cells that do not have a bomb.
- If a cell does not have a bomb, it will have a numeric value. That value is the number of adjacent bombs.
- You can mark cells as bombs, if you suspect they are a bomb.
"""

from IO.console_output import ConsoleOutput
from IO.str_to_int_validator import StrToIntValidator
from IO.console_input import ConsoleInput
from board_generator import BoardGenerator
from config.config_loader import ConfigLoader
from config.json_config_parser import JSONConfigParser
from engine import GameEngine
from menu import Menu

CONFIG_FILE_PATH = 'config.json'


def main():
    """Main function to bootstrap the game."""
    board_generator = BoardGenerator()
    config_parser = JSONConfigParser()
    config_loader = ConfigLoader(CONFIG_FILE_PATH, config_parser)
    console_input = ConsoleInput()
    console_output = ConsoleOutput()
    game_engine = GameEngine(board_generator)
    validator = StrToIntValidator()
    menu = Menu(config_loader, game_engine, console_input, console_output, validator)
    menu.run_main_menu()


if __name__ == '__main__':
    main()
