class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        rainl = self.get(height)
        height.reverse()
        rainr = self.get(height)
        rainr.reverse()
        return sum([min(rainl[i], rainr[i]) for i in range(n)])

    def get(self, height):
        begin = 0
        rain = []
        for h in height:
            if h >= begin:
                begin = h
                rain.append(0)
            else:
                rain.append(begin - h)
        return rain
