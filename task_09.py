def connect_dicts(dict1, dict2):
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())

    if sum1 > sum2:
        prim, second  = dict1, dict2
    else:
        prim, second = dict2, dict1

    new_dict = {k: v for k, v in second.items() if v >= 10}
    new_dict.update({k: v for k, v in prim.items() if v >= 10})

    res = dict(sorted(new_dict.items(), key=lambda item: item[1]))

    print(res)
    return res


connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }) # =>{ "c": 11, "b": 12 }
connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }) # =>{ d: 11, "c": 12, "a": 13 }
connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }) # =>{ "c": 11, "b": 12, "a": 15 }