from IO.base_output import BaseOutput


class ConsoleOutput(BaseOutput):
    def output(self, out: str) -> None:
        print(out)
