# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
I initially thought of slicing the prices array into days after the initial buy price and before. The idea is to find the max profit and do updates of the min_price and profit. (Just for practice, I needed a little help with chatGPT because it's getting late at night. :P)

# Approach
<!-- Describe your approach to solving the problem. -->
I initialized the min price with the first element of the array and the max profit. Update the minimum price, potential profit if that was the chosen buy point, and get the maximum profit. 

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(1)$$

# Code
```
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        min_price = prices[0]  # Initialize minimum price to the price on the first day
        max_profit = 0
        
        for price in prices[1:]:
            # Update the minimum price seen so far
            min_price = min(min_price, price)
            # Calculate the potential profit if selling at the current price
            potential_profit = price - min_price
            # Update the maximum profit seen so far
            max_profit = max(max_profit, potential_profit)
        
        return max_profit
```