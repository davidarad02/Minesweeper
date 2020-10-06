from abc import ABC, abstractmethod


class BaseOutput(ABC):
    """Defines abstraction for a string output device."""

    @abstractmethod
    def output(self, out: str) -> None:
        """
        Output text to destination.

        :param out: The value to be outputted.
        """
        ...
