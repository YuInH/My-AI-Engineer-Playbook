# LeetCode 121 - Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Step 1: Initiate max_profit as the final result of the algo, max_profit = 0
        # as base case, and min_price as float('inf') for general purpose
        max_profit = 0
        min_price = float('inf')

        # Step 2: Loop through the prices list
        for cur_price in prices:
            # Step 3: Set condition to assign min_price with actual minimum value
            if cur_price < min_price:
                min_price = cur_price
           
            # Step 4: Calculate profit as required
            profit = cur_price - min_price
           
            # Step 5: Set condition to assign max profit with the actual maximum value
            # of the possible profit from the list of transaction
            if profit > max_profit:
                max_profit = profit

        return max_profit
