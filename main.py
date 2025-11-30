import sys
from src.constants import Command
from src.helpers import parse_input
from src.handlers import compare_sorting_algorithms, merge_lists_handler

# Increase recursion limit fro being able to sort 1000 elem arrays
sys.setrecursionlimit(1100)


def main():
    print("Hello!")

    while True:
        command = parse_input(
            input(
                "Please, select the mode:"
                '\n-- for running comparison of sort algorithms print "c"'
                '\n-- for running sorted arrays merge print "m"'
                '\n-- for exiting the program print "q"'
                "\n"
            )
        )

        match command:
            case Command.QUIT:
                print("Goodbye!")
                break

            case Command.COMPARISON:
                compare_sorting_algorithms()
                break

            case Command.MERGE:
                merge_lists_handler()
                break

            case _:
                print("Invalid command. Please, use one of the listed below.")


if __name__ == "__main__":
    main()
