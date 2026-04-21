# LeetCode 1 - Two Sum (O(n) time complexity)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Step 1: Defining a "Storage": a Hashmap (dictionary) that'll store 1 number at
        # a time from nums[int] in a key-value pair
        # key: value of the element from the list
        # value: index of the element from the list
        storage = {}

        # Step 2: Loop through the nums list:
        for i, n in enumerate(nums):

            # Step 3: Defining the difference between the target and the current element:
            diff = target - n

            # Step 4: Check if diff is already in the storage: Return a list with:
            # storage{diff}: the key of diff, which stands for the index of the element
            # from the list
            # i: the index of the current element.
            if diff in storage:
                return [storage[diff], i]

            # Step 5: If not, add the current element and its' index into the storage
            storage[n] = i
        return