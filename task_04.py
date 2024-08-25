def sort_list(array):
    if not array: return []
    min_val = min(array)
    max_val = max(array)

    for i in range(len(array)):
        if array[i] == min_val:
            array[i] = max_val
        elif array[i] == max_val:
            array[i] = min_val

    array.append(min_val)
    print(array)
    return array


sort_list([]) # => []
sort_list([2, 4, 6, 8]) # => [8, 4, 6, 2, 2]
sort_list([1]) # => [1, 1]
sort_list([1, 2, 1, 3]) # => [3, 2, 3, 1, 1]