class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        test = [(abs(i), -i) for i in nums]
        test.sort()
        return -test[0][1]