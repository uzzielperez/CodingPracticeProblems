# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

Seemed easy but I forgot about the requirement to change the array ordering such that the first k elements of numbs contain the elements not equal to val. I felt like I had to loop through the array and just check whether the element is equal to the integer vals or nut.

# Approach
<!-- Describe your approach to solving the problem. -->
I iterated through the nums array and 


# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
It is linear time complexity, $$O(n)$$, where n is the length of the input array. The solution iterates from index 0 to the last index.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(1)$$ since the code only uses a constant amount of memory allocation.

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