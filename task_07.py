def combine_anagrams(words_array):
    anagrams = {}
    for word in words_array:
        sorted_word = ''.join(sorted(word)).lower()
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word.lower())
        else:
            anagrams[sorted_word] = [word.lower()]
    print(list(anagrams.values()))
    return list(anagrams.values())


combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"]) # => [ ["cars", "racs", "scar"], ["four"], ["for"],["potatoes"], ["creams", "scream"] 