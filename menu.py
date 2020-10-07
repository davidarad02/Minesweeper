from typing import List

from IO.base_input import BaseInput
from IO.base_output import BaseOutput
from IO.str_to_int_validator import StrToIntValidator
from config.config_loader import ConfigLoader
from engine import GameEngine
from game_mode import GameMode

GAME_MODES = 'game_modes'


class Menu:
    def __init__(self, config_loader: ConfigLoader, game_engine: GameEngine, input: BaseInput, output: BaseOutput,
                 str_to_int_validator: StrToIntValidator) -> None:
        """
        :param config_loader: Used to load configuration like the game modes.
        :param game_engine: The engine used to run games.
        :param input: Used to gather player input.
        :param output: Used to output data to the player.
        :param str_to_int_validator: Used to parse string inputs.
        """

        self._config_loader = config_loader
        self._game_engine = game_engine
        self._input = input
        self._output = output
        self._str_to_int_validator = str_to_int_validator

    def _game_options(self) -> List[GameMode]:
        """Make the game options array for the main menu."""

        options = [
            GameMode('Custom Game')
        ]
        config_game_modes = self._config_loader.load_config()[GAME_MODES]
        for game_mode in config_game_modes:
            options.append(GameMode.from_config_dict(game_mode))
        return options

    def _custom_game(self, custom_game_mode: GameMode) -> GameMode:
        """
        Create a custom game mode.

        :param custom_game_mode: The custom game mode object.
        :return: The inputted game mode object with modified properties.
        """
        self._output.output('Enter the width of the board: (4-50)')
        while True:
            valid_input, custom_game_mode.width = self._str_to_int_validator.validate_input(self._input.input(), 4, 51,
                                                                                            self._output)
            if valid_input:
                break
        self._output.output('Enter the height of the board: (4-50)')
        while True:
            valid_input, custom_game_mode.height = self._str_to_int_validator.validate_input(self._input.input(), 4, 51,
                                                                                             self._output)
            if valid_input:
                break
        max_bomb_count = custom_game_mode.height * custom_game_mode.width
        self._output.output(f'Enter the number of bombs on the board: (1-{max_bomb_count - 1})')
        while True:
            valid_input, custom_game_mode.bomb_count = self._str_to_int_validator.validate_input(self._input.input(), 1,
                                                                                                 max_bomb_count,
                                                                                                 self._output)
            if valid_input:
                break
        return custom_game_mode

    def run_main_menu(self) -> None:
        """Start the main menu to let the user start a game."""

        options = self._game_options()
        self._output.output('Welcome to Minesweeper!\n')
        while True:
            self._output.output('Main menu:\nPlease choose an option:')
            for index, value in enumerate(options):
                self._output.output(f'\t{index} - {value.name}')
            while True:
                selected_option = self._input.input()
                valid_input, selected_option = self._str_to_int_validator.validate_input(selected_option, 0,
                                                                                         len(options), self._output)
                if valid_input:
                    break
            game_mode = options[selected_option]
            if selected_option == 0:
                game_mode = self._custom_game(game_mode)
            self._game_engine.start_game(game_mode, self._input, self._output)
