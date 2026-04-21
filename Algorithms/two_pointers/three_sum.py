# LeetCode 15 - 3Sum (Handling duplicates)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Step 1: Create the res list to store the final result
        res = []

        # Step 2: Sort the "nums" list
        nums.sort()

        # Step 3: Loop through the list
        for i, a in enumerate(nums):

            # Step 4: Pass to next element if a duplicate is encountered
            if i > 0 and a == nums[i-1]:
                continue
           
            # Step 5: Two Pointer Method: l (left) on the position i + 1, r (right) on the end of the list
            l, r = i + 1, len(nums) - 1
           
            # Step 6: 2nd Loop performed until left element same as right element (means that all the elements on the list is reached)
            while l < r:
                threeSum = a + nums[l] + nums[r]
                # First condition of Two Pointer: if the "threeSum" is too big (> 0),
                # reduce right by 1 position (sorted list exclusive)
                if threeSum > 0:
                    r -= 1

                # Second condition of Two Pointer: if the "threeSum" is too small(< 0),
                # increase left by 1 position (also sorted list exclusive)
                elif threeSum < 0:
                    l += 1
               
                # Last condition of Two Pointer: if the "threeSum" is equal to 0, aka
                # met the requirement of the problem, we append the list of element a,
                # element of the list at left position and element of the list at
                # right position
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1

                    # Last step: After accepted the first sub string, put 1 more
                    # condition onto the last part to guarantee left will pass all the
                    # remaining duplicates
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
