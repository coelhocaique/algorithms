import file_reader as fr
import threading, sys, resource


class PivotType:
    LAST = 'LAST'
    FIRST = 'FIRST'
    MEDIAN_OF_THREE = 'MEDIAN_OF_THREE'

    @staticmethod
    def values():
        return [PivotType.LAST, PivotType.FIRST, PivotType.MEDIAN_OF_THREE]


def get_pivot(array, pivot_type, i, j):
    first, last = array[i], array[j-1]

    if pivot_type == PivotType.FIRST:
        pivot = first
        index = i
    elif pivot_type == PivotType.LAST:
        pivot = last
        index = j - 1
    elif pivot_type == PivotType.MEDIAN_OF_THREE:
        size = j - i
        mid_ind = ((i + j) // 2) - 1 if size % 2 == 0 else (i + j) // 2
        mid = array[mid_ind]
        mot = [[first, i], [mid, mid_ind], [last, j -1]]
        mot.sort()
        pivot, index = mot[1]

    return pivot, index


def partition(array, pivot_type, k, l):
    pivot, index = get_pivot(array, pivot_type, k, l)

    array[index] = array[k]
    array[k] = pivot

    i = k + 1

    for j in range(k, l):
        cur = array[j]

        if cur < pivot:
            array[j] = array[i]
            array[i] = cur
            i+=1

    array[k] = array[i-1]
    array[i-1] = pivot

    return array, i - 1


def quick_sort(array, pivot_type, comps, i, j):
    if abs(j - i) <= 1:
        return array, comps

    array, index = partition(array, pivot_type, i, j)
    array, comps_left = quick_sort(array, pivot_type, index - i - 1, i, index)
    array, comps_right = quick_sort(array, pivot_type, j - index, index + 1, j)

    return array, (comps + comps_left + comps_right)


def count_comparisons(numbers, pivot_type):
    if not type(numbers) == list:
        raise ValueError

    return quick_sort(numbers, pivot_type, 0, 0, len(numbers))


pivot_type = PivotType.MEDIAN_OF_THREE

numbers = fr.get_input_as_list(fr.FilePath.COMPARISONS)
numbers, comparisons = count_comparisons(numbers, pivot_type)

print('number of comparisons with pivot type %s = %d' % (pivot_type, comparisons))
