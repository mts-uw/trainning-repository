import random
from typing import List

# O(n^2)


def bubble_sort(numbers: List[int]) -> List[int]:

    for i in range(len(numbers)):
        for j in range(len(numbers)-1 - i):
            if numbers[j] >= numbers[j + 1]:
                tmp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = tmp

    return numbers


nums = [random.randint(0, 100) for _ in range(10)]
#nums = [2, 5, 1, 8, 7, 3]

print(bubble_sort(nums))
