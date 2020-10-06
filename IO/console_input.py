from IO.base_input import BaseInput


class ConsoleInput(BaseInput):
    def input(self) -> str:
        return `input()
