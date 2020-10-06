from abc import ABC, abstractmethod
from typing import Dict


class BaseConfigParser(ABC):
    """Abstraction to parse config."""
    @abstractmethod
    def parse_config(self, config_bytes: bytes) -> Dict:
        """Parse the given config and return it."""
        ...
