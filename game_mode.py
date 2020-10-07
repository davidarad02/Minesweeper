class GameMode:
    """Represents a single game mode."""

    def __init__(self, name: str = None, width: int = None, height: int = None, bomb_count: int = None) -> None:
        """
        :param name: The name of the mode.
        :param width: The width of the board in this mode.
        :param height: The height of the board in this mode.
        :param bomb_count: The number of bombs on the board in this mode.
        """
        self.name = name
        self.height = height
        self.width = width
        self.bomb_count = bomb_count

    @classmethod
    def from_config_dict(cls, config):
        obj = cls()
        obj.__dict__.update(config)
        return obj
