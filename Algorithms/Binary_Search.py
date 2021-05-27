def binary_search(arr, element):
    lower_bound = 0
    upper_bound = len(arr) - 1

    while lower_bound <= upper_bound:
        mid_index = (upper_bound + lower_bound) // 2

        if arr[mid_index] == element:
            return f"Number found at index: {mid_index}"

        else:
            if element > arr[mid_index]:
                lower_bound = mid_index+1
            else:
                upper_bound = mid_index-1
    return "Not Found"


ls = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 11, 21, 22]


print(binary_search(ls, 7))












