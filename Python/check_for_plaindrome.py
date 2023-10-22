def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    return s == s[::-1]


input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f"{input_string} is Palindrome")
else:
    print(f"{input_string} is not Palindrome")
