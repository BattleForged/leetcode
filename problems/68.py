class Solution:
    def getNextline(self, words, widthLeft):
        count = len(words)
        if count == 1:
            return words[0] + ' ' * widthLeft
        spaceLength = widthLeft // (count-1)
        spaceLeft = widthLeft % (count-1)
        nextLine = ''
        for i in range(count):
            if i != 0:
                nextLine += ' ' * spaceLength
                if i <= spaceLeft:
                    nextLine += ' '
            nextLine += words[i]
        return nextLine

    def getLastline(self, words, widthLeft):
        nextLine = ''
        count = len(words)
        for i in range(count):
            if i != 0:
                nextLine += ' '
                widthLeft -= 1
            nextLine += words[i]
        return nextLine + ' ' * widthLeft

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ret = []
        tmp = []
        widthLeft = maxWidth
        count = 0
        for word in words:
            length = len(word)
            if count != 0 and (widthLeft - length) // (count) < 1:
                nextLine = self.getNextline(tmp, widthLeft)
                ret.append(nextLine)
                tmp = []
                widthLeft = maxWidth
                count = 0
            tmp.append(word)
            widthLeft -= length
            count += 1
        nextLine = self.getLastline(tmp, widthLeft)
        ret.append(nextLine)
        return ret
