import sys
sys.path.append("..")
from utils.file_reader import *


def get_data():
    return list(map(lambda s: int(s), read_input(FilePath.INVERSIONS)))


def merge_sort(data):

    def split(left, right):
        c = []
        left_length, right_length = len(left), len(right)
        left_index, right_index, invs = 0, 0, 0

        for k in range(left_length + right_length):
            if left_index < left_length and right_index < right_length:
                cur_l, cur_r = left[left_index], right[right_index]
                if cur_l <= cur_r:
                    c.append(cur_l)
                    left_index += 1
                else:
                    c.append(cur_r)
                    invs += (left_length - left_index)
                    right_index += 1
            elif not left_index < left_length:
                c.append(right[right_index])
                right_index += 1
            else:
                c.append(left[left_index])
                left_index += 1

        return c, invs

    def sort(nums, invs, i, j):
        if abs(j - i) == 1:
            return [nums[i]], invs

        left, invs_left = sort(nums, invs, i, (i + j) // 2)
        right, invs_right = sort(nums, invs, (i + j) // 2, j)
        c, inv_split = split(left, right)

        return c, (invs_left + invs_right + inv_split)

    return sort(data, 0, 0, len(data))


def count_inversions(data):
    return merge_sort(data)


data = get_data()

numbers, inversions = count_inversions(data)

print('number of inversions = %d' % inversions)
