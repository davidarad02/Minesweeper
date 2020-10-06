from abc import ABC, abstractmethod

from board import Board


class BaseOutput(ABC):
    """Defines abstraction for a string output device."""

    @abstractmethod
    def output(self, out: str) -> None:
        """
        Output text to destination.

        :param out: The value to be outputted.
        """
        ...

    @abstractmethod
    def output_board(self, board: Board) -> None:
        """
        Output the current state of the board.

        :param board: The board to be outputted.
        """
        ...
