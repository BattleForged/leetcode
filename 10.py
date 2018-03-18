class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n1 = len(s)
        n2 = len(p)
        dp = [[False]*(n2+1) for i in range(n1+1)]
        dp[0][0] = True
        for i1 in range(n1+1):
            for i2 in range(n2):
                if dp[i1][i2]:
                    if i2 < n2-1 and p[i2+1] == '*':
                        dp[i1][i2+2] = True
                        if i1 < n1 and p[i2] == '.':
                            dp[i1+1][i2] = True
                        elif i1 < n1 and s[i1] == p[i2]:
                            dp[i1+1][i2] = True
                    elif p[i2] == '.' and i1 < n1:
                        dp[i1+1][i2+1] = True
                    elif i1 < n1 and s[i1] == p[i2]:
                        dp[i1+1][i2+1] = True
        return dp[n1][n2]
