from typing import Tuple

from IO.base_output import BaseOutput


class StrToIntValidator:
    def validate_input(self, input: str, range_min: int, range_max: int, output: BaseOutput) -> Tuple[bool, int]:
        """
        Validate the given input to be an integer within a range.

        :param input: The given input.
        :param range_min: The minimum value the input can be, inclusive.
        :param range_max: The maximum value the input can be, exclusive.
        :param output: Output device to signal the user.
        :return: The parsed input.
        """
        try:
            int_input = int(input)
        except ValueError:
            output.output('Input should be a number, try again:')
            return False, -1
        if range_min <= int_input < range_max:
            return True, int_input
        output.output(f'Input can only be between {range_min} and {range_max - 1}.')
        return False, -1
