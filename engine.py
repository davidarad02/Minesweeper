import re

from IO.base_input import BaseInput
from IO.base_output import BaseOutput
from board import Board
from board_generator import BoardGenerator
from errors.game_lost_error import GameLostError
from errors.game_won_error import GameWonError
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
        while True:
            try:
                self._process_single_turn(board, input, output)
            except GameLostError as e:
                output.output(f'BOOM! Game over! {tuple(x + 1 for x in e.args)} was a bomb!')
                break
            except GameWonError:
                output.output('Congratulations, you won!')
                break

    def _process_single_turn(self, board: Board, input: BaseInput, output: BaseOutput) -> None:
        """
        Run a single turn of the game.

        :param board: The board of the game.
        :param input: Used to gather player input.
        :param output: Used to output data to the player.
        """
        output.output_board(board)
        output.output('Enter x,y for cell and O to open, or M to mark, all comma-separated (example: 3,2,O)')
        x, y, operation = -1, -1, ''
        while True:
            user_action = input.input()
            matches = re.search('^(\d+),(\d+),([mMoO])$', user_action)
            if not matches:
                output.output('Input does not match the pattern! Try again:')
                continue
            x, y, operation = matches.groups()
            x, y = int(x) - 1, int(y) - 1
            if not 0 <= y < len(board.board) or not 0 <= x < len(board.board[y]):
                output.output('Input out of bounds! Try again:')
                continue
            break
        operation = operation.upper()
        actions = {
            'O': board.open_cell,
            'M': board.mark_cell
        }
        actions[operation](x, y)
