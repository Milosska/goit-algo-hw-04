from collections import deque


def merge_sort(arr: list[int]):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left: list[int], right: list[int]) -> list[int]:
    merged_array = []
    left_deque = deque(x for x in left)
    right_deque = deque(x for x in right)

    while left_deque and right_deque:
        if left_deque[0] <= right_deque[0]:
            merged_array.append(left_deque.popleft())
        else:
            merged_array.append(right_deque.popleft())

    merged_array.extend(left_deque)
    merged_array.extend(right_deque)

    return merged_array
