class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.n = len(s)
        depth = [0]
        now = 0
        for i in range(self.n):
            if s[i] == '(':
                now += 1
            else:
                now -= 1
            depth.append(now)
        ans0 = self.get(depth)
        depth.reverse()
        ans1 = self.get(depth)
        return ans0 if ans0 > ans1 else ans1

    def get(self, depth):
        ans = 0
        begin = 0
        end = 0
        while begin <= end and begin < self.n:
            if depth[end] == depth[begin]:
                if (end-begin) > ans:
                    ans = end - begin
            if depth[end] >= depth[begin]:
                if end < self.n:
                    end += 1
                else:
                    begin = end
            elif depth[end] < depth[begin]:
                begin = end
        return ans
