class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        k = [[m+n]*(n+1) for j in range(m+1)]
        for i in range(m+1):
            k[i][0] = i
        for i in range(n+1):
            k[0][i] = i
        for i in range(0, m+1):
            for j in range(0, n+1):
                if i < m and k[i+1][j] > k[i][j] + 1:
                    k[i+1][j] = k[i][j] + 1
                if j < n and k[i][j+1] > k[i][j] + 1:
                    k[i][j+1] = k[i][j] + 1
                if i < m and j < n:
                    if word1[i] == word2[j]:
                        if k[i+1][j+1] > k[i][j]:
                            k[i+1][j+1] = k[i][j]
                    else:
                        if k[i+1][j+1] > k[i][j] + 1:
                            k[i+1][j+1] = k[i][j] + 1
        return k[m][n]
