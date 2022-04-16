class Solution(object):
    @staticmethod
    def perhaps(l, ignore):
        ret = []
        for i in range(min(len(l), 3)):
            if l[i][1] != ignore:
                ret.append(l[i])
        return ret[0:2]

    def maximumScore(self, scores, edges):
        """
        :type scores: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(scores)
        m = len(edges)

        eBynode = []
        for i in range(n):
            eBynode.append([])
        for j in range(m):
            [a, b] = edges[j]
            eBynode[a].append((scores[b], b))
            eBynode[b].append((scores[a], a))
        for i in range(n):
            eBynode[i].sort(reverse=True)

        ret = -1
        for i in range(m):
            [a, b] = edges[i]
            now = scores[a]+scores[b]
            ap = Solution.perhaps(eBynode[a], b)
            bp = Solution.perhaps(eBynode[b], a)
            for aa in ap:
                for bb in bp:
                    if (aa[1] != bb[1]):
                        ret = max(ret, now + aa[0] + bb[0])
        return ret
