from src.constants import Command
from src.helpers import parse_input


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
                print("Comparison implementation")
                break

            case Command.MERGE:
                print("Merge implementation")
                break

            case _:
                print("Invalid command. Please, use one of the listed below.")


if __name__ == "__main__":
    main()
