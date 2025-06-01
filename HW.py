import timeit
import random


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


if __name__ == "__main__":

    sizes = [100, 10000, 50000]

    for size in sizes:
        data = [random.randint(0, 10000) for _ in range(size)]

        setup_insertion = f"from __main__ import insertion_sort; data = {data.copy()}"
        setup_merge = f"from __main__ import merge_sort; data = {data.copy()}"
        setup_tim = f"data = {data.copy()}"

        t_insertion = timeit.timeit("insertion_sort(data.copy())", setup=setup_insertion, number=1)
        t_merge = timeit.timeit("merge_sort(data.copy())", setup=setup_merge, number=1)
        t_tim = timeit.timeit("sorted(data.copy())", setup=setup_tim, number=1)

        print(f"\nSize: {size}")
        print(f"Insertion Sort: {t_insertion:.5f} seconds")
        print(f"Merge Sort: {t_merge:.5f} seconds")
        print(f"Timsort: {t_tim:.5f} seconds")