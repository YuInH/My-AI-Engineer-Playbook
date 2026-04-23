# LeetCode 11: Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Step 1: Initilize all the necessary variables
        n = len(height)
        l, r = 0, n - 1
        max_area = 0
        
        # Step 2: Two-pointer special: "while l < r" loop:
        while l < r:

            # Step 3: Calculate the Area of the container by width x height 
            area = (r - l) * min(height[l], height[r])

            # Step 4: Decide the max area by which one is greater
            max_area = max(area, max_area)
            
            # Step 5: Decide to move left or right by keeping the higher one
            if height[l] < height[r]:
                l += 1
            # Note: if height[l] == height[r], doesn't matter which one to move
            else:
                r -= 1

        return max_area