# Define the function is_palindrome
def is_palindrome(text):
    length = len(text)

# Use the for loop to compare the corresponding characters
    for i in range(0, length//2):
# Check if the corresponding characters are the same or not
        if text[i] != text[length-i-1]:
            return False # Return False if they don't match
    
    return True # Return True if they match

# Test function with a palindrome
string1 = "racecar"
print(is_palindrome(string1))

# Test function with a non-palindrome
string2 = "abceba"
print(is_palindrome(string2))