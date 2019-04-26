import file_reader as fr


class PivotType:
    LAST = 'LAST'
    FIRST = 'FIRST'
    MEDIAN_OF_THREE = 'MEDIAN_OF_THREE'

    @staticmethod
    def values():
        return [PivotType.LAST, PivotType.FIRST, PivotType.MEDIAN_OF_THREE]


def get_data():
    return list(map(lambda s: int(s), fr.read_input(fr.FilePath.COMPARISONS)))


def quick_sort(pivot_type):

    def find_pivot(array, i, j):
        first, last = array[i], array[j - 1]

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
            mot = [[first, i], [mid, mid_ind], [last, j - 1]]
            mot.sort()
            pivot, index = mot[1]

        return pivot, index

    def partition(array, k, l):
        pivot, index = find_pivot(array, k, l)

        array[index] = array[k]
        array[k] = pivot

        i = k + 1
        for j in range(k, l):
            cur = array[j]
            if cur < pivot:
                array[j] = array[i]
                array[i] = cur
                i += 1

        array[k] = array[i - 1]
        array[i - 1] = pivot

        return array, i - 1

    def sort(array, comps, i, j):
        if abs(j - i) <= 1:
            return array, comps

        array, index = partition(array, i, j)
        array, comps_left = sort(array, index - i - 1, i, index)
        array, comps_right = sort(array, j - index, index + 1, j)

        return array, (comps + comps_left + comps_right)

    data = get_data()

    return sort(data, 0, 0, len(data))


def count_comparisons(pivot_type):
    return quick_sort(pivot_type)


pivot_type = PivotType.MEDIAN_OF_THREE

numbers, comparisons = count_comparisons(pivot_type)

print('number of comparisons with pivot type %s = %d' % (pivot_type, comparisons))
