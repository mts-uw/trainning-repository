from typing import List


def list_max_sum(numbers: List[int]) -> int:
    numbers = [i for i in numbers if i >= 0]
    print(numbers)
    if not numbers:
        return 0
    else:
        return sum(numbers)


n = int(input())
a = list(map(int, input().split()))
print(list_max_sum(a))
