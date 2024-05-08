# Отсортируйте данный список таким образом,
# чтобы его элементы оказались в порядке убывания частоты их появления,
# то есть по количеству раз, которое они появляются в элементах.
# Если два элемента имеют одинаковую частоту, они должны оказаться в своем естественном порядке.
# assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
# assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
#     4,
#     4,
#     4,
#     3,
#     3,
#     11,
#     11,
#     7,
#     13,
# ]

from collections import Counter
from typing import Iterable

def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    counter = Counter(numbers)
    sorted_numbers = sorted(numbers, key=lambda x: (-counter[x], x))
    return sorted_numbers
