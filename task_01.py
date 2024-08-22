def is_palindrome(string):
    if isinstance(string, int):
        string = str(string)
    if string is None or not isinstance(string, str):
        return False
    
    normalized = ''
    for char in string.lower():
        if char.isalnum():
            normalized+= char
    return normalized == normalized[::-1]


print(
is_palindrome("A man, a plan, a canal -- Panama") # => True
    
)
print(
is_palindrome("Madam, I'm Adam!") # => True
    
)
print(
is_palindrome(333) # => True
    
)
print(
is_palindrome(None) # => False
    
)
print(
is_palindrome("Abracadabra") # => False
    
)
