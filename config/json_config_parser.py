import json
from typing import Dict

from config.base_config_parser import BaseConfigParser


class JSONConfigParser(BaseConfigParser):
    """Parse a given JSON config."""
    def parse_config(self, config_bytes: bytes) -> Dict:
        return json.loads(config_bytes)