from IO.base_input import BaseInput
from IO.base_output import BaseOutput
from board_generator import BoardGenerator
from game_mode import GameMode


class GameEngine:
    def __init__(self, board_generator: BoardGenerator):
        """
        :param board_generator: Used to generate new boards for new games.
        """

        self._board_generator = board_generator

    def start_game(self, game_mode: GameMode, input: BaseInput, output: BaseOutput) -> None:
        """
        Start a new game.

        :param game_mode: The mode to run the game at.
        :param input: Used to gather player input.
        :param output: Used to output data to the player.
        """
        board = self._board_generator.generate_board(game_mode.height, game_mode.width, game_mode.bomb_count)
        # while True:
