def insertion_sort(array: list[int], index=1) -> list[int]:
    if index == len(array):
        return array

    element = array[index]
    current_index = index - 1

    while current_index >= 0 and array[current_index] > element:
        array[current_index + 1] = array[current_index]
        current_index -= 1

    array[current_index + 1] = element

    return insertion_sort(array, index + 1)
