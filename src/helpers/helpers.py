from src.decorators.decorators import handle_errors
from src.constants import Command


@handle_errors
def parse_input(user_input):
    if user_input is None:
        raise ValueError("Invalid command. Please, use one of the listed below.")

    normalized_input = user_input.strip().lower()
    command = Command(normalized_input)
    return command
