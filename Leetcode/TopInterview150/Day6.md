# Day 6: Majority
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
I thought it was easy at first, i.e. from the pattern I could just slice the nums list into the last k parts and the first k-len(nums) part and then do the switcheroo. So I thought
# Approach
<!-- Describe your approach to solving the problem. -->
I encountered issues with larger inputs and for cases where k > len(nums). The trick was to do k%=n to reduce the number of rotations k to the number of rotations.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$ - linear time complexity
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$ - constant space complexity due to creating a and b
# Code
```
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # So you don't really have to do the rotation k times if k >n
        k %= n 
        
        a = nums[len(nums)-k:]
        b = nums[:len(nums)-k]
        nums[:] = a + b 
    

        # i = 0 
        # while i < k:
        #   nums.insert(0, nums.pop())
        #   i+=1

        ## Both solutions below don't work for large inputs
        # a = nums[len(nums)-k:]
        # b = nums[:len(nums)-k]
        # nums[:] = a + b 
    
     

     

            
        
```