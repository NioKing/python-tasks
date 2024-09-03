def max_odd(array):
    res = None

    def flattenArray(ar):
        nonlocal res
        for a in ar:
            if isinstance(a, list):
                flattenArray(a)
            elif isinstance(a, (float, int)) and a % 2 == 1:
                if res is None or a > res:
                    res = a

    flattenArray(array)
    print(int(res) if res else None)
    return int(res) if res else None

max_odd([1, 2, 3, 4, 4]) # => 3
max_odd([21.0, 2, 3, 4, 4]) # => 21
max_odd(['ololo', 2, 3, 4, [1, 2], None]) # => 3
max_odd(['ololo', 'fufufu']) # => None
max_odd([2, 2, 4]) # => None