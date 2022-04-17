class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        cnt = {}
        for i in tasks:
            cnt[i] = cnt.get(i, 0) + 1
        ret = 0
        for k, v in cnt.items():
            if (v%3 == 0):
                ret += v//3
            elif (v>2 and (v-2)%3==0):
                ret += (v-2)//3 + 1
            elif (v>4 and (v-4)%3==0):
                ret += (v-4)//3 + 2
            else:
                return -1
        return ret