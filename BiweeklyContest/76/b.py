class Solution(object):
    def waysToBuyPensPencils(self, total, cost1, cost2):
        """
        :type total: int
        :type cost1: int
        :type cost2: int
        :rtype: int
        """
        ret = 0
        for i in range(total  // cost1 + 1):
            ret += (total - cost1 * i) // cost2 + 1
        return ret