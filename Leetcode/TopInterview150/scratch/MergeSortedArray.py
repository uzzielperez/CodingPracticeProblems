import itertools

# Case 1
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]

# Case 2 Failed at first because only last 3 zeroes are to be ignored.
nums1 = [-1,0,0,3,3,3,0,0,0]
nums2 = [1,2,2]


# nums = nums1[:3]

print ( "nums1: ", nums1 )
print ( "nums2: ", nums2 )


# First remove the last few zeros 
# nums1.pop(0)
i = len(nums1) - 1 

# while i >= 0:
#     if nums1[i] == 0:
#         nums1.pop(i)
#     i -= 1

for e2 in nums2:
    nums1.pop(i)
    i -= 1

for e2 in nums2:
    nums1.append(e2)
    
    
# nums1 = sorted(nums1)
nums1.sort()


####### FAILED Solution

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for e2 in nums2:
	        nums1.append(e2)


        i = len(nums1) - 1 

        while i >= 0:
            if nums1[i] == 0:
                nums1.pop(i)
        i -= 1

        nums1 = sorted(nums1)
		
	
		


# for e2 in nums2:
# 	for e1 in nums1:
# 		if e1 == 0:
# 			print (e1, e2)
# 			nums1[j] = e2
# 			nums2.pop(i)
# 			j +=1 
# 	i +=1



print ("nums1:" , nums1)


# for i, j in nums, nums2:
# 	print (i, j)
# 	if i < j:
# 		nums.append(j)
# 	elif i > j:
# 		nums[i+1] = nums[i]
# 		nums[i]   = nums2[j]
		
# print (nums)
