nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

nums = nums1[:3]

for i, j in nums, nums2:
	print (i, j)
	if i < j:
		nums.append(j)
	elif i > j:
		nums[i+1] = nums[i]
		nums[i]   = nums2[j]
		
print (nums)
