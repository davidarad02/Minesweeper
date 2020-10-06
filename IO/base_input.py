from abc import ABC, abstractmethod


class BaseInput(ABC):
    """Defines abstraction for a string input device."""

    @abstractmethod
    def input(self) -> str:
        """
        Input text from source.

        :return: Gathered input.
        """
        ...
