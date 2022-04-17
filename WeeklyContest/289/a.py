class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ret = s
        while len(ret) < k:
            newRet = ''
            sum = 0
            for i in range(len(ret)):
                sum += ord(ret[i]) - ord('0')
                if (i%k == k-1):
                    newRet += str(sum)
                    sum = 0
            if (len(ret)%k != 0):
                newRet += str(sum)