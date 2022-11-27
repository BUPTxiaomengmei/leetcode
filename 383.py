class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i,'',1)
                ransomNote = ransomNote.replace(i,'',1)
        if ransomNote == '':
            return True
        else:
            return False

solution = Solution()
print(solution.canConstruct('aaaa','aabaa'))