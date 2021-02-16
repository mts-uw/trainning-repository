import random
from typing import List


def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)

    for i in range(len_numbers):
        temp = numbers[i]

        j = i - 1

        while j >= 0 and numbers[j] > temp:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = temp

    return numbers


def bucket_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    len_numbers = len(numbers)
    size = max_num // len(numbers)

    buckets = [[] for _ in range(size)]
    for num in numbers:
        i = num // size
        if i != size:
            buckets[i].append(num)

        else:
            buckets[size - 1].append(num)

    for i in range(size):
        insertion_sort(buckets[i])

    result = []
    for i in range(size):
        result += buckets[i]

    return result


nums = [random.randint(0, 100) for _ in range(10)]
print(bucket_sort(nums))
