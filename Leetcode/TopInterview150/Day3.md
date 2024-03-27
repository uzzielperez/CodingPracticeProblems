# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
It seemed easy at first since you just needed to see the element the first time and have a separate list of nonduplicates.
The tricky part is you need to modify the list as you are iterating over the elements. The judge matters.

# Approach
<!-- Describe your approach to solving the problem. -->
The trick was to do nums[:] after you've selected the nonduplicates. Doing only nums = first will not affect the original nums list. Doing nums[:], makes a shallow copy of nums and ensures that the changes will be reflected back to the original.


# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)∗O(1)=O(n)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

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