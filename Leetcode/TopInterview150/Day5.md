# Day 5: Majority
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
I was thinking of doing a dict/map cut I wanted a simpler solution which checks the for majority and breaks the search loop when found.
# Approach
<!-- Describe your approach to solving the problem. -->
I iterate through the elements and use the count function to check if nums.count(e) > n/2. If that condition is satisfied, the search is over and there is no need to look at the rest of the numbers in the list.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$ - linear time complexity
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(1)$$ - constant space complexity
# Code
```
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj = 0 

        for e in nums:
            if nums.count(e) > len(nums)/2:
                maj = e
                break
    
        return maj
        
```