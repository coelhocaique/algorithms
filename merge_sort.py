import file_reader as fr


def inversion_split(left, right):
    c = []
    left_length, right_lenght = len(left), len(right)
    left_index, right_index, invs = 0, 0, 0

    for k in range(left_length + right_lenght):
        if left_index < left_length and right_index < right_lenght:
            cur_l, cur_r = left[left_index], right[right_index]
            if cur_l <= cur_r:
                c.append(cur_l)
                left_index+=1
            else:
                c.append(cur_r)
                invs +=(left_length - left_index)
                right_index+=1
        elif not left_index < left_length:
            c.append(right[right_index])
            right_index+=1
        else:
            c.append(left[left_index])
            left_index+=1

    return c, invs


def inversion(nums, invs, i, j):
    if abs(j - i) == 1:
        return [nums[i]], invs

    left, invs_left = inversion(nums, invs, i, (i + j) // 2)
    right, invs_right = inversion(nums, invs, (i + j) // 2, j)
    c, inv_split = inversion_split(left, right)

    return c, (invs_left + invs_right + inv_split)


def count_inversions(numbers):
    if not type(numbers) == list:
        raise ValueError

    return inversion(numbers, 0, 0, len(numbers))


numbers = fr.get_input_as_list(fr.FilePath.INVERSIONS)

numbers, inversions = count_inversions(numbers)

print('number of inversions = %d' % inversions)
