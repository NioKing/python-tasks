def coincidence(list=[], range=0):
    if not list or not range:
        return []
    max = 0
    min = 99999
    res = []
    for r in range:
        if max < r:
            max = r
        if min > r:
            min = r
    
    for v in list:
        if isinstance(v, (int, float)) and v <= max and v >= min:
            res.append(v);
    print(res)
    return res


coincidence([1, 2, 3, 4, 5], range(3, 6)) # => [3, 4, 5]
coincidence() # => []
coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)) # => [1, 2, 2.5]