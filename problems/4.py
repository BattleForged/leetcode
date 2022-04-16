class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        mid_point = (n - 1) / 2 # n=3, mid_point=1;n=6, mid_point=2(and 3)
        if n % 2 == 1:
            even = 0
        else:
            even = 1
        i1 = 0
        i2 = 0
        mid = 0
        for i in range(0, mid_point + even + 1):
            if i1 < n1 and i2 < n2 and nums1[i1] <= nums2[i2]:
                if i >= mid_point:
                    mid += nums1[i1]
                i1 += 1
            elif i1 < n1 and i2 < n2 and nums1[i1] > nums2[i2]:
                if i >= mid_point:
                    mid += nums2[i2]
                i2 += 1
            elif i1 == n1:
                if i >= mid_point:
                    mid += nums2[i2]
                i2 += 1
            else:
                if i >= mid_point:
                    mid += nums1[i1]
                i1 += 1
        if even == 1:
            mid /= 2.0
        return mid
