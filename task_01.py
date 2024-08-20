def is_palindrome(string):
    string.lower()
    if string == string[::-1] and string != None:
        return True
    else:
        return False

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
