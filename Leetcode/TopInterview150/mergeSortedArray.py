class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1) - 1

        for e2 in nums2:
            nums1.pop(i)
            i -= 1

        for e2 in nums2:
            nums1.append(e2)

        nums1.sort()


