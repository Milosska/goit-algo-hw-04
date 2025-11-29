import random


# Generates a list of random integers with controlled repetitions.
# Creates an array of 1/5 length of the given size
# Shuffles and duplicates this base list 5 times to introduce repetitions
def generate_random_numbers_in_range(size: int) -> list[int]:
    if not isinstance(size, int):
        raise ValueError("Size should be integer.")

    part_of_array: list[int] = []
    for i in range(1, ((size // 5) + 1)):
        number = random.randrange(1, size + 1)
        part_of_array.append(number)

    random_numbers: list[int] = []
    for i in range(1, 6):
        random.shuffle(part_of_array)
        random_numbers.extend(part_of_array)

    return random_numbers


def generate_uniquie_numbers_in_range(size: int) -> list[int]:
    if not isinstance(size, int):
        raise ValueError("Size should be integer.")

    return random.sample(range(1, size + 1), size)
