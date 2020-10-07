BOMB_VALUE = -1
EMPTY = 0


class Cell:
    """Represents a single cell on the minesweeper board."""

    def __init__(self, value: int, opened: bool = False, marked: bool = False):
        """
        :param value: The value of the cell - aka how many bombs it has adjacent.
        If `value` is `BOMB_VALUE`, it is considered a bomb.
        :param opened: Whether the cell has already been opened.
        :param marked: Whether the call has been marked as a bomb by the player.
        """
        self._value = value
        self._opened = opened
        self._marked = marked

    @property
    def value(self) -> int:
        """Get the read-only value of the cell - a cell does not change its value over the game."""
        return self._value

    @property
    def opened(self) -> bool:
        """Get the read-only `_opened` value."""
        return self._opened

    @property
    def marked(self):
        """Get the read-only '_marked` value."""
        return self._marked

    @property
    def is_bomb(self) -> bool:
        """Check if a cell is a bomb. A bomb cell is defined as a cell with a value of `BOMB_VALUE`."""
        return self._value == BOMB_VALUE

    def open(self) -> None:
        """Set the cell to be opened."""
        self._marked = False  # An open cell cannot be marked.
        self._opened = True

    def mark(self) -> None:
        """Mark or unmark a cell as a bomb. Marking a marked cell will remove the mark."""
        self._marked = not self._marked
