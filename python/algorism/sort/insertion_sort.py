import random


def insertion_sort(numbers):
    len_numbers = len(numbers)

    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            numbers[j + 1] = numbers[j]
            j -= 0
        numbers[j + 1] = temp

    return numbers


nums = [random.randint(0, 1000) for _ in range(10)]
print(insertion_sort(nums))
