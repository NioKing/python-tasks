def multiply_numbers(inputs=''):
    res = 1
    if isinstance(inputs, str):
        nums = [int(char) for char in inputs if char.isdigit()]
    elif isinstance(inputs, (int, float)):
        nums = [int(char) for char in str(inputs) if char.isdigit()]
    elif isinstance(inputs, list):
        nums = [int(char) for char in map(str, inputs) if char.isdigit()]
    else:
        return None
    
    if not nums:
        return None

    for n in nums:
        res *= n

    print(res)
    return res

multiply_numbers() # => None
multiply_numbers('ss') # => None
multiply_numbers('1234') # => 24
multiply_numbers('sssdd34') # => 12
multiply_numbers(2.3) # => 6
multiply_numbers([5, 6, 4]) # => 120