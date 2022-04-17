class Solution(object):
    def maxTrailingZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        simple = []
        for i in range(m):
            simpleList = []
            for j in range(n):
                simpleList.append(Solution.calculate(grid[i][j]))
            simple.append(simpleList)

        h = []
        for i in range(m):
            hList = []
            now = (0, 0)
            for j in range(n):
                now = Solution.plus(now, simple[i][j])
                hList.append(now)
            h.append(hList)
        
        v = []
        for i in range(n):
            vList = []
            now = (0, 0)
            for j in range(m):
                now = Solution.plus(now, simple[j][i])
                vList.append(now)
            v.append(vList)

        ret = 0
        for i in range(m):
            for j in range(n):
                now = simple[i][j]
                for i0 in [h[i][j], Solution.plus(Solution.minus(h[i][n-1],h[i][j]), now)]:
                    for j0 in [v[j][i], Solution.plus(Solution.minus(v[j][m-1],v[j][i]), now)]:
                        test = Solution.minus(Solution.plus(i0, j0), now)
                        ret = max(min(test[0], test[1]),ret)
        return ret

    @staticmethod
    def calculate(now):
        had5 = 0
        while(now % 5 == 0):
            had5 += 1
            now //= 5
        had2 = 0
        while(now % 2 == 0):
            had2 += 1
            now //= 2
        return (had2, had5)
    
    @staticmethod
    def plus(a, b):
        return (a[0]+b[0], a[1]+b[1])

    @staticmethod
    def minus(a, b):
        return (a[0]-b[0], a[1]-b[1])