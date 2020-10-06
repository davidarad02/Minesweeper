from typing import Dict

from config.base_config_parser import BaseConfigParser


class ConfigLoader:
    """Loads and parses the config file."""

    def __init__(self, config_file_path: str, parser: BaseConfigParser):
        """
        :param config_file_path: The path to the configuration file.
        :param parser: The parser used to parse the contents of the file.
        """
        self._config_file_path = config_file_path
        self._parser = parser

    def load_config(self) -> Dict:
        """Load the given config file to a dictionary."""
        with open(self._config_file_path, 'rb') as config_file:
            return self._parser.parse_config(config_file.read())
