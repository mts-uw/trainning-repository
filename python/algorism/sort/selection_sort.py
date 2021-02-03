import random
from typing import List


def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_idx = i
        for j in range(i + 1, len_numbers):
            if numbers[min_idx] > numbers[j]:
                min_idx = j

        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    return numbers


nums = [random.randint(0, 100) for _ in range(10)]
#nums = [2, 5, 1, 8, 7, 3]

print(selection_sort(nums))
