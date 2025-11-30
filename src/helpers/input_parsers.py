from src.decorators.decorators import handle_errors
from src.constants import Command


@handle_errors
def parse_input(user_input: str) -> Command:
    if user_input is None:
        raise ValueError("Invalid command. Please, use one of the listed below.")

    normalized_input = user_input.strip().lower()
    command = Command(normalized_input)
    return command


def parse_lists_number(user_input: str) -> int:
    normalized_input = user_input.strip()

    if not normalized_input.isnumeric():
        raise ValueError("Invalid value. Please, indicate number of lists.")

    value = int(normalized_input)
    if value < 2 or value > 100:
        raise ValueError("Invalid value. Please indicate number between 2 and 100.")

    return value


def parse_list(user_input: str) -> list[int]:
    normalized_input = user_input.strip()

    if not normalized_input:
        raise ValueError("List is empty. Please, provide valid list.")

    parsed_values_array: list[int] = []
    values_array = normalized_input.split()
    for elem in values_array:
        try:
            parsed_values_array.append(int(elem))
        except ValueError:
            raise ValueError(f"Invalid number: '{elem}'. All values must be integers.")

    return parsed_values_array
