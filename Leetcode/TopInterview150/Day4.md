# Day 3 Remove Duplicates from Sorted Array (Python)
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
It's the same as the previous problem, i.e. we create an extra empty list and append the element if it's not already there. The issue was tracking how many times it appears in the list.


# Approach
<!-- Describe your approach to solving the problem. -->
This time, we need to count the number of times it appears. If it appears 2 or more times then we have to reset the counter and skip to the next element. If the element is already in twice, we can append it to the list provided the count is equal to one.


# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n^2)$$ since you iterate through the n elements in nums and have to search for in the twice list in the worst-case scenario that each of the n elements appear twice in the original list nums.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$ because of the twice list.

# Code
```
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0

        for e in nums:
            if e != val:
                nums[i] = e
                i +=1 
        return i

```