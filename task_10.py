def count_words(string):
    map = {}
    normalized_string = ''.join(char for char in string if char.isalnum() or char.isspace()).lower()
    words = normalized_string.split()

    for word in words:
        map[word] = (map.get(word) or 0) + 1
    
    print(map)
    return map

count_words("A man, a plan, a canal -- Panama") # => {"a": 3, "man": 1,"canal": 1, "panama": 1, "plan": 1}
count_words("Doo bee doo bee doo") # => {"doo": 3, "bee": 2}