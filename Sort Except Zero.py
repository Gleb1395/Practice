# Відсортуй числа в списку. Але положення нулів змінювати не варто
# assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
# assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
# assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
# assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
from collections.abc import Iterable


def except_zero(items: list[int]) -> Iterable[int]:
    copy_lst = items[:]
    sort_lst = []
    for element in items:
        if element == 0:
            sort_lst.append(element)
        else:
            count_zero = copy_lst.count(0)
            if count_zero >= 1:
                for zero in range(count_zero + 1):
                    index = copy_lst.index(min(copy_lst))
                    if copy_lst[index] == 0:
                        copy_lst.pop(index)
            min_element = min(copy_lst)
            sort_lst.append(min_element)
            copy_lst.pop(copy_lst.index(min(copy_lst)))
    return sort_lst
