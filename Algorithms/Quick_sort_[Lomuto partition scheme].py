def swap(index_a, index_b, arr):
    if index_a != index_b:
        arr[index_a], arr[index_b] = arr[index_b], arr[index_a]


def partition(arr, start, end):
    pivot = arr[end]
    p_index = start

    while arr[p_index] != pivot:
        while p_index < len(arr) and arr[p_index] < pivot:
            p_index += 1

        i = p_index
        while i < len(arr) and arr[i] > pivot:
            i += 1

        swap(i, p_index, elements)
    return p_index


def quick_sort(arr, start, end):
    if start < end:
        partition_point = partition(elements, start, end)
        quick_sort(elements, start, partition_point-1)
        quick_sort(elements, partition_point + 1, end)


if __name__ == '__main__':
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')


