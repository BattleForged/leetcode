class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_length = [0] * (n+1)
        now_times = 0
        for i in range(n):
            if max_length[now_times] < i:
                now_times += 1
            could = i + nums[i]
            if max_length[now_times] < could:
                if max_length[now_times+1] < could:
                    max_length[now_times+1] = could
        return now_times
