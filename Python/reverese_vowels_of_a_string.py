class Solution(object):
    def reverseVowels(self, s):
        # Function to reverse only the vowels in the string 's'.
        """
        :type s: str
        :rtype: str
        """

        # String containing all the vowels (both lower and upper case).
        vowels = "aeiouAEIOU"

        # Convert the input string 's' into a list 's_list' to modify individual characters.
        s_list = list(s)

        # Initialize two pointers 'left' and 'right' to the beginning and end of the list 's_list'.
        left, right = 0, len(s_list) - 1

        # Loop until 'left' is less than 'right'.
        while left < right:

            # Find the leftmost vowel in the string 's_list'.
            # Continue searching until 'left' is less than 'right' and the character at 'left' is not a vowel.
            while left < right and s_list[left].lower() not in vowels:
                # Move 'left' pointer to the right.
                left += 1

            # Find the rightmost vowel in the string 's_list'.
            # Continue searching until 'left' is less than 'right' and the character at 'right' is not a vowel.
            while left < right and s_list[right].lower() not in vowels:
                # Move 'right' pointer to the left.
                right -= 1

            # If 'left' is still less than 'right', it means we found vowels that need to be swapped.
            if left < right:

                # Swap the characters at 'left' and 'right' positions in 's_list'.
                s_list[left], s_list[right] = s_list[right], s_list[left]

                # Move 'left' pointer to the right.
                left += 1
                # Move 'right' pointer to the left.
                right -= 1

        # Join the modified 's_list' back into a string and return the result.
        return "".join(s_list)

# Test the function
# Input string to test the 'reverseVowels' function.
input_string = "Hello World"

# Call the 'reverseVowels' function with the input string.
result = Solution().reverseVowels(input_string)

# Print the result of reversing the vowels in the input string.
print("Reversed vowels string:", result)