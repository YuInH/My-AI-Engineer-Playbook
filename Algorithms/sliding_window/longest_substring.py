# LeetCode 3 - Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Step 1: Create:
        #           - A longest variable for storing the result
        #           - A subString dictionary for storing the character by a 
        # character-index pair 
        #           - A left variable for the left side of the sliding window
        longest = 0
        subString = {}
        left = 0
        # Step 2: Loop through the string's letters, create right variable for the 
        # right side of the sliding window:
        for right, character in enumerate(s):
            # Step 3: Whenever the character at "right" position is found in the 
            # current sub string, move "left" to the position right after the position 
            # of the first encounter of this character.  
            if character in subString and subString[character] >= left:
                left = subString[character] + 1

            # Step 4: Storing (or Restoring) the position of the current character 
            # with the value of the current "right" position
            subString[character] = right

            # Step 5: Count the length of the sub string by the formula:
            # (right - left) + 1, and chose the longest by the larger bewteen: the old
            # longest value and the new sub string length
            window = (right - left) + 1
            longest = max(longest, window)

        return longest