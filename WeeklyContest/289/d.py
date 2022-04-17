import heapq

class Solution(object):
    def longestPath(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        child = [[]for i in range(len(s))]
        for i, j in enumerate(parent):
            if j >= 0:
                child[j].append(i)
        res = [0]
        def dfs(i):
            candi = [0, 0]
            for j in child[i]:
                cur = dfs(j)
                if s[i] != s[j]:
                    candi.append(cur)
                    
            candi = heapq.nlargest(2, candi)
            res[0] = max(res[0], candi[0] + candi[1] + 1)
            return max(candi) + 1
        
        dfs(0)
        return res[0]